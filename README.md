# Data-Source-API-Analyst-Test
Homework assignment for Data Source API Analyst role.
Step 1: Prepare & Test a List of Reports
1. Understand Client Needs:
○ Search Repositories (public)
○ Commits
○ Contents
2. Research GitHub API:
○ Identify the endpoints necessary to cover the client's needs.
○ Research for API documentation to understand Requests Logic, Pagination, Rate
limits, Error Handling, etc.
Step 2: Set Up a GitHub Repository
1. Create a New Repository with some name e.g.Data-Source-API-Analyst-Test.
○ Add a description like, "Homework assignment for Data Source API Analyst role."
○ Set the repository as Public
2. Repository Structure
○ README.md: Describe the purpose of each part of the test and provide brief
documentation of your approach. Also, for Part 5 you can add your reflection to
the assignment.
○ /Content: Add files here related to:
■ API Documentation
■ Python code for the auth process, data extraction, handling errors, rate
limits, and pagination.
■ Include troubleshooting guides and data-cleaning approach documents
here.
○ /Postman_Collection: Add a Postman collection or Jupyter notebook used in
Google Colab to this folder.
3. Commit Files
○ Please commit the folder structure and README to provide context, which will
serve as a foundation for creating API requests using Postman or Google Colab.
Step 3: Create a Postman Collection or Google Colab Notebook for API
Extraction
1. Set Up Postman or Google Colab
○ If using Postman:
■ Create a new collection called Github API Test.
■ Add folders e.g. Auth or Requests if needed.
■ Set up requests for each API endpoint you plan to test.
○ If using Google Colab:
■ Create a new Colab notebook.
■ Set up Python code to make API requests.
■ Include cells for each API endpoint you’re testing.
2. Extract Data Using API
○ In Postman:
■ Define environment variables (e.g., Authorization,
X-GitHub-Api-Version) for each API to streamline requests.
■ Send requests to retrieve data and view the response structure.
■ Save each response for reference.
○ In Colab:
■ Write functions to handle authentication, rate limits, and pagination.
■ Use loops to extract data over time, handling pagination if needed.
■ Print response samples for validation.
○ Note: Using the Google Colab approach will earn you bonus points.
Step 4: Troubleshooting Guide
1. Identify Common Issues
○ If you encounter a “401 Unauthorized” error:
■ Check Authentication: Verify the AUTH_TOKEN or access token. Ensure
it’s active and has the necessary permissions.
■ Environment Variables: Make sure the environment variables in
Postman are correctly set.
■ Rate Limits: Some APIs restrict the number of requests within a given
timeframe. Document handling of these limits in Colab or Postman using
error handling.
Step 5: Get Result
● Save the result file to your Github repo:
○ Export Postman Collection as a .json file.
○ Download the Colab notebook as a .ipynb file
