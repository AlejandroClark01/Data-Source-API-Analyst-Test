import requests
import time

def get_all_commits(token, owner, repo, max_pages=3):
    headers = {"Authorization": f"Bearer {token}"}
    all_commits = []
    for page in range(1, max_pages + 1):
        url = f"https://api.github.com/repos/{owner}/{repo}/commits?page={page}&per_page=30"
        r = requests.get(url, headers=headers)
        if r.status_code == 403:
            print("Rate limited. Waiting...")
            time.sleep(60)
            continue
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        all_commits.extend(data)
    return all_commits
