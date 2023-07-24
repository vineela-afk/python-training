import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PHISHTANK_API_URL = "https://checkurl.phishtank.com/checkurl/index.php"

def check_phishing_url(url):
    params = {
        "url": url,
        "format": "json",
        "app_key": "<APP_KEY>"
    }
    try:
        response = requests.post(PHISHTANK_API_URL, data=params, verify=False)
        data = response.json()
        if "results" in data:
            result = data["results"]["url"]
            if result["in_database"] == "yes" and result["valid"] == "yes":
                return f"{url} is a phishing URL."
        return f"{url} is not a phishing URL."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
