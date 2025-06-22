def get_github_headers(token: str) -> dict:
    """
    Returns the authorization headers for GitHub API requests.
    """
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
