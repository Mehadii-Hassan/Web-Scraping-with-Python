import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

first_quote = soup.find("div", class_="quote")
print(first_quote)