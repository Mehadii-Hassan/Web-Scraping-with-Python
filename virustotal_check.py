import requests
import base64

API_KEY = "a20aba6198df620392eea3ef0eda03646cd3c43693a3212f071b6ea20eec5dc8"


def check_virustotal(url):
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    headers = {
        "x-apikey": API_KEY
    }
    api_url = f"https://www.virustotal.com/api/v3/urls/{encoded_url}"

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code != 200:
            return "Error"

        stats = response.json()["data"]["attributes"]["last_analysis_stats"]
        if stats["malicious"] > 0 or stats["suspicious"] > 0:
            return "Yes"
        else:
            return "No"
    except Exception as e:
        return "Error"
