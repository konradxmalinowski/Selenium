import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
# dopasuj ścieżkę
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

service = Service('geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)

# Otwórz Wikipedię
driver.get('https://www.wikipedia.org/')
time.sleep(2)

# Wyszukaj pole tekstowe i wpisz zapytanie
search_box = driver.find_element(By.ID, 'searchInput')
search_box.send_keys('OpenAI')
search_box.submit()

# Czekaj, żeby zobaczyć wyniki
time.sleep(5)

driver.quit()
