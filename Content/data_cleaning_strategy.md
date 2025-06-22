# Data Cleaning Strategy

## Raw GitHub Data Challenges:
- Long nested JSON objects
- Redundant fields
- Nullable/missing keys

## Cleaning Steps:
- Extract only essential fields (e.g. repo name, stars, language, created_at)
- Normalize commits or contents into flat structures
- Convert timestamps to readable formats
- Drop null fields before saving to JSON/CSV
