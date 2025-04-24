import csv

import requests
from bs4 import BeautifulSoup

from step4_extract_text_author import quote_text, author

url = "http://quotes.toscrape.com"
resposne = requests.get(url)
soup = BeautifulSoup(resposne.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

with open("quotes.csv", mode = "w", newline= "", encoding="utf-8") as file :
    writer = csv.writer(file)
    writer.writerow(["serial", "Quote", "Author"])

    for index, quote in enumerate(quotes, start = 1):
        quote_text = quote.find("span", class_= "text").text
        author = quote.find("small", class_= "author").text
        writer.writerow([index, quote_text, author])