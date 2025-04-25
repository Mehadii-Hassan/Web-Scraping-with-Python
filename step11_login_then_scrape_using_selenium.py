from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/login")

username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
username_input.send_keys("admin")
password_input.send_keys("admin")

login_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
login_button.click()

time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "quote")
for index, quote in enumerate(quotes, start=1):
    quote_text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f"{index}. {quote_text} — {author}")

driver.quit()
