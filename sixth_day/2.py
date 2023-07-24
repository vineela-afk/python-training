import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PHISHTANK_API_URL = "https://checkurl.phishtank.com/checkurl/index.php"

def check_phishing_url(url):
    params = {
        "url": url,
        "format": "json",
        "app_key": "<APP_KEY>"
    }
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        response = session.post(PHISHTANK_API_URL, data=params, verify=False)
        data = response.json()
        if "results" in data:
            result = data["results"]["url"]
            if result["in_database"] == "yes" and result["valid"] == "yes":
                return f"{url} is a phishing URL."
        return f"{url} is not a phishing URL."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"


