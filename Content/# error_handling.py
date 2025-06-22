import requests

def safe_get(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
