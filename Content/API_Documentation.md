# GitHub API Documentation Summary

This document outlines the GitHub REST API endpoints used for this test.

## Tools Used
-  Postman — to manually test endpoints and validate responses
-  Google Colab — to programmatically extract and process GitHub data

---

## 1. Search Public Repositories
- Endpoint: `GET https://api.github.com/search/repositories?q={query}`
- Tested in: Postman + Python
- Notes: Used `per_page`, `page` for pagination

## 2. List Commits for a Repository
- Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/commits`
- Tested in: Postman + Python
- Notes: Used pagination via `?page=1&per_page=30`

## 3. Get Repository Contents
- Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/contents/`
- Tested in: Postman + Python
- Notes: Tested on `freeCodeCamp/freeCodeCamp`
