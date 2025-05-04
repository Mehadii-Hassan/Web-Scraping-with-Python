import requests
from bs4 import BeautifulSoup
import re

def extract_emails_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        return ', '.join(set(emails)) if emails else "Not found"
    except:
        return "Failed"
