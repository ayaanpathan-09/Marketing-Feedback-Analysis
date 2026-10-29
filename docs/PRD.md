# Product Requirements Document (PRD)
## 1. Product overview
**Product name:** Marketing Feedback Analysis Dashboard  
**Purpose:** Help marketing teams understand customer feedback and identify potential improvements to campaigns, channels, and products.

## 2. Problem statement
Customer comments and ratings can be spread across channels and are difficult to review manually. Teams need a simple way to summarize feedback, estimate sentiment, compare campaigns, and inspect individual comments.

## 3. Goals
- Summarize feedback volume, ratings, and estimated sentiment.
- Compare sentiment and ratings across campaigns, channels, and products.
- Let analysts upload a CSV rather than requiring a database connection.
- Enable filtered feedback export for further investigation.

## 4. Target users
- Marketing analysts
- Digital marketing teams
- Customer experience teams
- Students demonstrating data analytics skills

## 5. User stories
1. As a marketing analyst, I want to upload feedback data so I can analyze my own campaign results.
2. As a campaign manager, I want to compare sentiment by campaign and channel.
3. As a customer experience analyst, I want to search comments containing a specific word.
4. As a stakeholder, I want to export filtered records for a report.

## 6. Scope
### In scope
- CSV upload and sample dataset
- Data validation and normalization
- Sentiment scoring and labels
- KPI cards, charts, filters, keyword counts
- Filtered CSV download
- Documentation and basic tests

### Out of scope
- Live social media listening or API integrations
- User accounts and role-based access
- Automatic marketing campaign execution
- Production-grade multilingual sentiment analysis
- Cloud deployment and database persistence

## 7. Success measures
- A user can start the app locally using the README.
- Valid CSV data loads without manual code changes when it contains `feedback_text`.
- Filters update metrics, charts, and table consistently.
- Users can download the filtered data.
- Unit tests for sentiment labeling pass.

## 8. Assumptions and constraints
- Input is a CSV file.
- Feedback data is authorized for analysis and has personal identifiers removed.
- Sentiment is an estimate and should not be treated as a definitive measure of customer intent.
- Included records are synthetic demonstration data.

## 9. Risks
- Sarcasm, slang, mixed language, and context may reduce sentiment accuracy.
- Small or biased feedback samples may not represent all customers.
- Inconsistent campaign names can fragment comparisons.

## 10. Future enhancements
- Connect approved review/social APIs.
- Add multilingual models and aspect-based sentiment.
- Add database storage, authentication, and scheduled reports.
- Add campaign-level statistical confidence and trend alerts.
