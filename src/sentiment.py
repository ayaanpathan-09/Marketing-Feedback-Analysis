from __future__ import annotations
import re

POSITIVE_WORDS = {
    "good", "great", "excellent", "love", "loved", "helpful", "easy", "fast",
    "amazing", "happy", "satisfied", "recommend", "useful", "clear", "best",
    "friendly", "smooth", "quality", "wonderful", "perfect", "affordable"
}
NEGATIVE_WORDS = {
    "bad", "poor", "hate", "hated", "slow", "difficult", "confusing", "expensive",
    "disappointed", "disappointing", "unhappy", "broken", "issue", "problem",
    "late", "worst", "waste", "annoying", "spam", "misleading", "unhelpful"
}

def analyze_sentiment(text: str) -> tuple[str, float]:
    """Return (label, compound_score). Uses VADER if available, otherwise a basic fallback."""
    text = str(text or "")
    try:
        from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
        analyzer = SentimentIntensityAnalyzer()
        score = float(analyzer.polarity_scores(text)["compound"])
    except Exception:
        tokens = re.findall(r"[a-z']+", text.lower())
        pos = sum(token in POSITIVE_WORDS for token in tokens)
        neg = sum(token in NEGATIVE_WORDS for token in tokens)
        score = (pos - neg) / max(1, pos + neg + 1)
    label = "Positive" if score >= 0.05 else ("Negative" if score <= -0.05 else "Neutral")
    return label, round(score, 4)

def add_sentiment(df):
    out = df.copy()
    result = out["feedback_text"].apply(analyze_sentiment)
    out["sentiment"] = result.apply(lambda x: x[0])
    out["sentiment_score"] = result.apply(lambda x: x[1])
    return out
