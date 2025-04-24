import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

first_quote = soup.find("div", class_="quote")

quote_text = first_quote.find("span", class_="text").text
author = first_quote.find("small", class_="author").text

print("Quote:", quote_text)
print("Author:", author)