# Marketing Feedback Analysis Dashboard

A complete beginner-friendly Python + Streamlit project for analyzing customer feedback about marketing campaigns, products, and customer experience.

## Features
- Interactive dashboard with KPI cards: total feedback, average rating, positive/neutral/negative sentiment.
- Sentiment analysis using VADER when installed, with a lightweight rule-based fallback.
- Feedback filters for campaign, channel, product, sentiment, and date.
- Visualizations for sentiment, ratings, channel performance, campaign performance, and feedback volume over time.
- Common keyword/theme exploration.
- Upload your own CSV and download filtered results.
- Documentation included: PRD, TRD, FRD, and data structure.

## Important note about the included data
`data/sample_feedback.csv` is a **synthetic sample dataset** created for demonstration and testing. It is not real customer data. Use the upload feature to analyze your own authorized feedback data.

## Requirements
- Python 3.10 or newer recommended
- pip

## Run in VS Code (Windows)
1. Extract the ZIP file.
2. Open the extracted `marketing-feedback-analysis` folder in VS Code.
3. Open Terminal → New Terminal.
4. Create a virtual environment (recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
5. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
6. Start the dashboard:
   ```powershell
   python -m streamlit run app.py
   ```
7. Streamlit will show a local URL, usually `http://localhost:8501`.

If PowerShell blocks activation, skip activation and run:
```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Input CSV format
Required column:
- `feedback_text`

Recommended optional columns:
- `feedback_id`, `feedback_date`, `rating`, `campaign`, `channel`, `product`, `customer_segment`

Column names are case-insensitive. If optional columns are missing, the app fills them with safe defaults. Date format should be parseable by pandas; rating should be between 1 and 5.

## Project structure
```text
marketing-feedback-analysis/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── sample_feedback.csv
├── docs/
│   ├── PRD.md
│   ├── TRD.md
│   ├── FRD.md
│   ├── DATA_STRUCTURE.md
│   └── TEST_PLAN.md
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── sentiment.py
│   └── analytics.py
└── tests/
    └── test_sentiment.py
```

## Data privacy
Do not upload sensitive personal information. Remove names, phone numbers, email addresses, order IDs, and other direct identifiers before analysis. Only use feedback you are authorized to process.

## Troubleshooting
- **`streamlit` is not recognized:** use `python -m streamlit run app.py`.
- **No module named pandas/streamlit:** install dependencies with `python -m pip install -r requirements.txt`.
- **CSV upload error:** check that the file is a CSV and contains a `feedback_text` column.
- **VADER missing:** install requirements; the app still has a simple fallback, but VADER is recommended for better sentiment quality.
