from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from src.data_loader import normalize_feedback
from src.sentiment import add_sentiment
from src.analytics import top_keywords

st.set_page_config(page_title="Marketing Feedback Analysis", page_icon="📊", layout="wide")

ROOT = Path(__file__).parent
SAMPLE_PATH = ROOT / "data" / "sample_feedback.csv"

@st.cache_data
def load_sample():
    return pd.read_csv(SAMPLE_PATH)

@st.cache_data
def prepare_data(raw_df):
    normalized = normalize_feedback(raw_df)
    return add_sentiment(normalized)

st.title("📊 Marketing Feedback Analysis Dashboard")
st.caption("Turn customer comments into actionable marketing insights. Included data is synthetic demo data.")

with st.sidebar:
    st.header("Data source")
    uploaded = st.file_uploader("Upload feedback CSV", type=["csv"])
    st.markdown("---")
    st.caption("Required column: `feedback_text`")
    st.caption("Optional: date, rating, campaign, channel, product, customer_segment")

try:
    if uploaded is not None:
        raw = pd.read_csv(uploaded)
        data = prepare_data(raw)
        st.sidebar.success(f"Loaded {len(data):,} feedback records from your CSV.")
    else:
        data = prepare_data(load_sample())
        st.sidebar.info("Showing the included synthetic sample dataset.")
except Exception as exc:
    st.error(f"Could not load the data: {exc}")
    st.stop()

with st.sidebar:
    st.header("Filters")
    campaigns = sorted(data["campaign"].dropna().astype(str).unique().tolist())
    channels = sorted(data["channel"].dropna().astype(str).unique().tolist())
    products = sorted(data["product"].dropna().astype(str).unique().tolist())
    sentiments = ["Positive", "Neutral", "Negative"]
    selected_campaigns = st.multiselect("Campaign", campaigns, default=campaigns)
    selected_channels = st.multiselect("Channel", channels, default=channels)
    selected_products = st.multiselect("Product", products, default=products)
    selected_sentiments = st.multiselect("Sentiment", sentiments, default=sentiments)
    min_date = pd.to_datetime(data["feedback_date"]).min().date()
    max_date = pd.to_datetime(data["feedback_date"]).max().date()
    date_range = st.date_input("Feedback date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

filtered = data[
    data["campaign"].astype(str).isin(selected_campaigns)
    & data["channel"].astype(str).isin(selected_channels)
    & data["product"].astype(str).isin(selected_products)
    & data["sentiment"].isin(selected_sentiments)
].copy()

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        pd.to_datetime(filtered["feedback_date"]).dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.warning("No feedback matches these filters. Change one or more filters.")
    st.stop()

total = len(filtered)
avg_rating = filtered["rating"].mean()
positive_pct = (filtered["sentiment"].eq("Positive").mean() * 100)
negative_pct = (filtered["sentiment"].eq("Negative").mean() * 100)
rated = filtered["rating"].notna().sum()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total feedback", f"{total:,}")
c2.metric("Average rating", f"{avg_rating:.2f}/5" if pd.notna(avg_rating) else "N/A")
c3.metric("Positive sentiment", f"{positive_pct:.1f}%")
c4.metric("Negative sentiment", f"{negative_pct:.1f}%")
c5.metric("Ratings received", f"{rated:,}")

st.markdown("---")
left, right = st.columns(2)

with left:
    st.subheader("Sentiment distribution")
    sentiment_counts = filtered["sentiment"].value_counts().reindex(["Positive", "Neutral", "Negative"], fill_value=0)
    fig, ax = plt.subplots()
    sentiment_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of feedback entries")
    ax.tick_params(axis="x", rotation=0)
    st.pyplot(fig, clear_figure=True)

with right:
    st.subheader("Average rating by channel")
    rating_by_channel = filtered.dropna(subset=["rating"]).groupby("channel")["rating"].mean().sort_values(ascending=False)
    if rating_by_channel.empty:
        st.info("No valid ratings available in this selection.")
    else:
        fig, ax = plt.subplots()
        rating_by_channel.plot(kind="bar", ax=ax)
        ax.set_ylim(0, 5)
        ax.set_ylabel("Average rating (out of 5)")
        ax.set_xlabel("Channel")
        ax.tick_params(axis="x", rotation=25)
        st.pyplot(fig, clear_figure=True)

left, right = st.columns(2)
with left:
    st.subheader("Sentiment by campaign")
    campaign_sentiment = pd.crosstab(filtered["campaign"], filtered["sentiment"]).reindex(columns=["Positive", "Neutral", "Negative"], fill_value=0)
    if not campaign_sentiment.empty:
        fig, ax = plt.subplots()
        campaign_sentiment.plot(kind="bar", stacked=True, ax=ax)
        ax.set_ylabel("Feedback count")
        ax.set_xlabel("Campaign")
        ax.tick_params(axis="x", rotation=25)
        st.pyplot(fig, clear_figure=True)

with right:
    st.subheader("Feedback volume over time")
    daily = filtered.assign(feedback_date=pd.to_datetime(filtered["feedback_date"]).dt.date).groupby("feedback_date").size().sort_index()
    fig, ax = plt.subplots()
    daily.plot(kind="line", marker="o", ax=ax)
    ax.set_xlabel("Date")
    ax.set_ylabel("Feedback count")
    ax.tick_params(axis="x", rotation=25)
    st.pyplot(fig, clear_figure=True)

st.markdown("---")
st.subheader("Common words and themes")
keywords = top_keywords(filtered["feedback_text"].tolist(), limit=15)
if keywords:
    kw_df = pd.DataFrame(keywords, columns=["Keyword", "Mentions"])
    st.dataframe(kw_df, use_container_width=True, hide_index=True)
else:
    st.info("Not enough text to extract keywords.")

st.subheader("Feedback explorer")
search_text = st.text_input("Search feedback text", placeholder="e.g. delivery, discount, helpful")
view = filtered.copy()
if search_text.strip():
    view = view[view["feedback_text"].str.contains(search_text.strip(), case=False, na=False)]
columns = ["feedback_id", "feedback_date", "rating", "sentiment", "sentiment_score", "campaign", "channel", "product", "customer_segment", "feedback_text"]
st.dataframe(view[columns].sort_values("feedback_date", ascending=False), use_container_width=True, hide_index=True)

csv_bytes = view[columns].to_csv(index=False).encode("utf-8")
st.download_button("Download filtered feedback (CSV)", data=csv_bytes, file_name="filtered_marketing_feedback.csv", mime="text/csv")

with st.expander("How to interpret this dashboard"):
    st.markdown("""
    - **Positive/negative sentiment** is an automated estimate of the wording, not a guaranteed understanding of customer intent.
    - **Average rating** only includes rows with a valid rating from 1 to 5.
    - **Common words** are simple frequency counts, not advanced topic modeling.
    - Compare campaigns only when they have enough feedback and similar collection methods.
    - The sample data is synthetic. Conclusions from it are only for demonstrating the app.
    """)
