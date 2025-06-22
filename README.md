---

##  Project Overview & Approach

This assignment demonstrates how to interact with the GitHub REST API using two tools: **Postman** and **Google Colab**. Each part of the test focuses on a core skill required for a data source analyst working with APIs.

###  Part-by-Part Summary

####  Part 1 – Understand & Prepare Reports
- Identified key API features: public repo search, commit logs, and repo contents.
- Analyzed documentation to understand endpoint structure, parameters, rate limits, and authentication.

####  Part 2 – GitHub Repository Setup
- Created public GitHub repo with well-structured folders: `/Content`, `/Postman_Collection`.
- Wrote brief documentation (`README.md`) and included technical scripts, troubleshooting steps, and API notes.

####  Part 3 – API Extraction via Postman and Colab
- Built a Postman collection with all core endpoints for quick testing.
- Wrote modular Python functions in Colab for automated data extraction, pagination, and response validation.

####  Part 4 – Troubleshooting
- Documented and handled common errors like `401 Unauthorized`, `403 Rate Limit`, and `404 Not Found`.
- Used `try/except`, response codes, and backoff timing in Colab to handle API limitations smoothly.

####  Part 5 – Final Output & Reflection
- Exported and committed both Postman Collection (`.json`) and Colab notebook (`.ipynb`) to the repo.
- All files follow clear naming conventions and are organized for easy navigation.

---

##  Reflection (Part 5)

This assignment deepened my understanding of how to work with REST APIs in real-world scenarios. While Postman is great for initial testing and visual validation, Google Colab allowed me to automate the full flow, handle pagination, and build reusable functions  a crucial step in scaling API usage for real data pipelines.

One challenge I encountered was managing GitHub rate limits and getting 404s when paths were incorrect — this helped me improve my error-handling logic and become more methodical with endpoint construction.

Overall, this was a great exercise in thinking like a data engineer: understanding the data source, validating response structures, and building scripts to reliably extract and process information.

---
