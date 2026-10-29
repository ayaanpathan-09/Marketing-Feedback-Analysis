# Data Structure / Data Dictionary
## 1. Input CSV schema

| Field | Type | Required | Description | Example |
|---|---|---:|---|---|
| `feedback_id` | string | No | Unique feedback identifier; generated if absent | FB-00001 |
| `feedback_date` | date/datetime | No | Date feedback was received | 2026-10-01 |
| `rating` | integer/float | No | Customer rating from 1 to 5 | 4 |
| `campaign` | string | No | Campaign name | Diwali Sale |
| `channel` | string | No | Feedback/marketing channel | Email |
| `product` | string | No | Product or service name | Starter Plan |
| `customer_segment` | string | No | Broad customer segment | Returning |
| `feedback_text` | string | **Yes** | Customer comment/review text | “The offer was easy to use.” |

## 2. Derived fields
| Field | Type | Description |
|---|---|---|
| `sentiment` | category | Positive, Neutral, or Negative |
| `sentiment_score` | float | Compound sentiment estimate, generally -1 to +1 |

## 3. Relationships
This project uses a single flat feedback table. `feedback_id` identifies a row. Campaign, channel, product, and customer segment are dimensions used to group feedback. There is no relational database in this version.

## 4. Data quality rules
- `feedback_text` must be present and non-empty.
- Ratings must be within 1–5; invalid values are treated as missing.
- Invalid/missing dates are replaced with a safe date value.
- Missing category fields are filled with `Unspecified`.
- Use anonymized, authorized data only.

## 5. Example CSV
```csv
feedback_id,feedback_date,rating,campaign,channel,product,customer_segment,feedback_text
FB-00001,2026-10-01,5,Diwali Sale,Email,Starter Plan,Returning,"The offer was clear and easy to use."
```
