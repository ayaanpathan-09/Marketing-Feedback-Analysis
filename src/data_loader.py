from __future__ import annotations
import pandas as pd

REQUIRED_COLUMNS = ["feedback_text"]
OPTIONAL_DEFAULTS = {
    "feedback_id": None,
    "feedback_date": None,
    "rating": None,
    "campaign": "Unspecified",
    "channel": "Unspecified",
    "product": "Unspecified",
    "customer_segment": "Unspecified",
}

def normalize_feedback(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and normalize feedback CSV data to the app's standard schema."""
    if df is None or df.empty:
        raise ValueError("The uploaded dataset is empty.")
    out = df.copy()
    out.columns = [str(c).strip().lower().replace(" ", "_") for c in out.columns]
    if "feedback_text" not in out.columns:
        # Allow a common alternative, but do not guess from arbitrary columns.
        alternatives = {"comment": "feedback_text", "review": "feedback_text", "feedback": "feedback_text"}
        for old, new in alternatives.items():
            if old in out.columns:
                out = out.rename(columns={old: new})
                break
    if "feedback_text" not in out.columns:
        raise ValueError("CSV must include a 'feedback_text' column (or comment/review/feedback).")

    for col, default in OPTIONAL_DEFAULTS.items():
        if col not in out.columns:
            out[col] = default

    if out["feedback_id"].isna().all():
        out["feedback_id"] = [f"FB-{i+1:05d}" for i in range(len(out))]
    else:
        out["feedback_id"] = out["feedback_id"].fillna("").astype(str)
        blank = out["feedback_id"].str.strip().eq("")
        out.loc[blank, "feedback_id"] = [f"FB-{i+1:05d}" for i in range(int(blank.sum()))]

    if out["feedback_date"].isna().all():
        out["feedback_date"] = pd.Timestamp.today().normalize()
    out["feedback_date"] = pd.to_datetime(out["feedback_date"], errors="coerce")
    if out["feedback_date"].isna().all():
        out["feedback_date"] = pd.Timestamp.today().normalize()
    else:
        out["feedback_date"] = out["feedback_date"].fillna(out["feedback_date"].median())

    out["rating"] = pd.to_numeric(out["rating"], errors="coerce")
    out.loc[~out["rating"].between(1, 5), "rating"] = pd.NA

    for col in ["campaign", "channel", "product", "customer_segment"]:
        out[col] = out[col].fillna("Unspecified").astype(str).str.strip()
        out.loc[out[col].eq(""), col] = "Unspecified"

    out["feedback_text"] = out["feedback_text"].fillna("").astype(str).str.strip()
    out = out[out["feedback_text"].ne("")].copy()
    if out.empty:
        raise ValueError("No non-empty feedback text was found.")
    return out.reset_index(drop=True)
