# data_extraction.py
import requests

def search_repositories(token, query="data analytics", per_page=5):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/search/repositories?q={query}&per_page={per_page}"
    return requests.get(url, headers=headers).json()

def get_commits(token, owner, repo, per_page=5):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page={per_page}"
    return requests.get(url, headers=headers).json()

def get_repo_contents(token, owner, repo, path=""):
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    return requests.get(url, headers=headers).json()
