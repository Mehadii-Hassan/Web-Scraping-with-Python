import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for index, quote in enumerate(quotes, start = 1):
    quote_text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{index}. {quote_text} - {author}")