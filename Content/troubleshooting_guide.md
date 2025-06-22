# Troubleshooting Guide

## Common Issues & Fixes

### ❌ 404 Not Found
- ✅ Make sure repo/owner/path exists
- ✅ Ensure repo is public or token has permission

### ❌ 403 Rate Limited
- ✅ Check rate with `GET /rate_limit`
- ✅ Add auth token to boost to 5000 requests/hour

### ❌ 401 Unauthorized
- ✅ Double-check token in Authorization headers

### ❌ Empty Response
- ✅ Try `per_page` and `page` parameters to debug paging
