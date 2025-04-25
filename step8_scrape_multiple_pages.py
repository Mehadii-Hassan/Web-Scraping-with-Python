import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "Quotes"
sheet.append(["Serial", "Quote", "Author"])

base_url = "http://quotes.toscrape.com/page/{}/"
serial = 1

for page in range(1, 11) :
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes :
        break

    for quote in quotes :
        quote_text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        sheet.append([serial, quote_text, author])
        serial = serial + 1

wb.save("all_quotes.xlsx")