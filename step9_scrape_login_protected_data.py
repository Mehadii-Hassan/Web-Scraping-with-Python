import requests
from bs4 import BeautifulSoup

session = requests.Session()
login_url = "http://quotes.toscrape.com/login"
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

csrf_token = soup.find("input", {"name": "csrf_token"}).get("value")

login_data = {
    "csrf_token": csrf_token,
    "username" : "admin",
    "password" : "admin"
}

response = session.post(login_url, data = login_data)

quotes_page = session.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(quotes_page.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for index, quote in enumerate(quotes, start=1):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    print(f"{index}. {text} - {author}")