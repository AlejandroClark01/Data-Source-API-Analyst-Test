# GitHub API Documentation Summary

This document outlines the GitHub API endpoints used in this project.

---

## 1. Search Public Repositories
- Endpoint: `GET https://api.github.com/search/repositories?q={query}`
- Purpose: Returns repositories matching a search query

## 2. List Commits for a Repository
- Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/commits`
- Supports: `per_page`, `page` for pagination

## 3. Get Repository Contents
- Endpoint: `GET https://api.github.com/repos/{owner}/{repo}/contents/{path}`
- Purpose: Lists files and folders in a repo

## 4. Rate Limits
- Endpoint: `GET https://api.github.com/rate_limit`
- Purpose: Check remaining API calls
