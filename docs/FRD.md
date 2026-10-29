# Functional Requirements Document (FRD)
## FR-01: Load sample data
The app shall load `data/sample_feedback.csv` when no upload is provided.

## FR-02: Upload user data
The user shall be able to upload a CSV file. The CSV shall contain `feedback_text`, or an accepted alternative (`comment`, `review`, `feedback`).

## FR-03: Normalize input
The system shall standardize column names, add missing optional columns, parse dates, validate ratings, and exclude empty feedback text.

## FR-04: Sentiment analysis
The system shall assign Positive, Neutral, or Negative sentiment and a numeric score to each feedback entry.

## FR-05: Filter feedback
The user shall be able to filter by campaign, channel, product, sentiment, and date range.

## FR-06: Display KPIs
The dashboard shall show total feedback, average valid rating, positive percentage, negative percentage, and count of rated entries.

## FR-07: Visualize feedback
The dashboard shall display sentiment distribution, average rating by channel, sentiment by campaign, and feedback volume over time.

## FR-08: Keyword exploration
The dashboard shall show common non-stopword terms from the currently filtered comments.

## FR-09: Search comments
The user shall be able to search feedback text by a text substring.

## FR-10: Export
The user shall be able to download the visible filtered feedback as a CSV.

## FR-11: Explain limitations
The app shall explain that sentiment is an estimate and sample data is synthetic.

## FR-12: Error messages
The app shall show understandable errors for empty files, unsupported files, and missing feedback text.
