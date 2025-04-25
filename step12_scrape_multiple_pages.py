import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/page/{}/"
page = 1

while True:
    response = requests.get(base_url.format(page))
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if not quotes:
        break

    print(f"\n📄 Page {page}")
    for index, quote in enumerate(quotes, start=1):
        quote_text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f"{index}. {quote_text} — {author}")

    page = page + 1
