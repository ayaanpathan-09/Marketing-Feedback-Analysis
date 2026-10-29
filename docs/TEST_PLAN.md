# Test Plan
## Manual test cases
| ID | Test | Expected result |
|---|---|---|
| TC-01 | Run app with no upload | Sample dashboard loads |
| TC-02 | Upload valid CSV | Records load and KPIs update |
| TC-03 | Upload CSV with no feedback text column | Clear validation error |
| TC-04 | Upload CSV with blank comments | Blank rows excluded |
| TC-05 | Filter to one campaign | KPIs, charts, and table reflect selection |
| TC-06 | Search for a word | Table shows matching comments only |
| TC-07 | Download filtered CSV | CSV contains the visible filtered rows |
| TC-08 | Rating outside 1–5 | Invalid rating excluded from average |

## Automated tests
Run:
`python -m unittest discover -s tests -v`
