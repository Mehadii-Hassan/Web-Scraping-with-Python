import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

wb = Workbook()
sheet = wb.active
sheet.title = "Quotes"

sheet.append(["Serial", "Quate", "Author"])

for index, quote in enumerate (quotes, start=1):
    quote_text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    sheet.append([index, quote_text, author])

wb.save("quotes.xlsx")