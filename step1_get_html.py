import requests

url = "http://quotes.toscrape.com"
response = requests.get(url)

print(response)
print(response.text)