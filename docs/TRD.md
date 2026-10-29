# Technical Requirements Document (TRD)
## 1. Architecture
The application is a local Streamlit dashboard with a small Python analytics layer.

```text
CSV file / sample CSV
        |
        v
src/data_loader.py  -> validate, normalize, clean
        |
        v
src/sentiment.py    -> sentiment label and score
        |
        v
src/analytics.py    -> common keyword frequency
        |
        v
app.py              -> filters, KPIs, charts, table, CSV export
```

## 2. Technology stack
- Python 3.10+
- Streamlit: user interface
- pandas / NumPy: tabular processing
- Matplotlib: charts
- VADER Sentiment: English sentiment estimation
- pytest: optional unit-test runner

## 3. Runtime requirements
- Desktop/laptop with Python and pip
- Internet required only to install dependencies
- No API key is required
- No database is required
- CSV file should fit available memory

## 4. Data processing
1. Read the uploaded CSV.
2. Normalize column names to lowercase with underscores.
3. Validate that `feedback_text` exists (also accepts `comment`, `review`, or `feedback`).
4. Add missing optional columns with defaults.
5. Parse dates and ratings; ratings outside 1–5 become missing.
6. Remove blank feedback text.
7. Score sentiment and label each record.
8. Apply sidebar filters and calculate aggregates.

## 5. Sentiment logic
VADER compound score is used when the dependency is available:
- Positive: score >= 0.05
- Neutral: -0.05 < score < 0.05
- Negative: score <= -0.05

If VADER cannot be imported, a simple positive/negative word-count fallback is used. This fallback is intentionally basic.

## 6. Security and privacy
- No data is transmitted by application code to an external service.
- Uploaded data is processed in the local Streamlit session.
- Do not use sensitive personal data; anonymize direct identifiers first.
- If deployed, configure access controls and data retention appropriate to the organization.

## 7. Performance
- Suitable for small and medium CSV datasets that fit in RAM.
- Streamlit caching is used for data loading and preparation.
- Very large datasets may need sampling, a database, or batch processing.

## 8. Error handling
- Missing feedback text column: display a clear error.
- Empty CSV or blank feedback: display a clear error.
- Missing optional fields: use defaults.
- Invalid dates/ratings: coerce to missing or safe defaults.

## 9. Installation and execution
See the root README. Main command:
`python -m streamlit run app.py`
