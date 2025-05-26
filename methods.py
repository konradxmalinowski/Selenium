# selenium_locators_example.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Konfiguracja przeglądarki Firefox
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # ścieżka do przeglądarki

service = Service('geckodriver.exe')  # ścieżka do geckodrivera
driver = webdriver.Firefox(service=service, options=options)

# Otwórz stronę główną Wikipedii
driver.get("https://www.wikipedia.org/")
time.sleep(2)

# 1. By.ID - wybór elementu po atrybucie "id"
search_input = driver.find_element(By.ID, "searchInput")
search_input.send_keys("OpenAI")

# 2. By.NAME - wybór elementu po atrybucie "name"
# Na tej stronie nie ma inputa z name="search", ale pokazujemy przykład:
# input_by_name = driver.find_element(By.NAME, "search")

# 3. By.CLASS_NAME - wybór po klasie CSS (musi być jedna, bez spacji)
search_lang_button = driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive")
# Kliknięcie przycisku (lub możesz submitować formularz)
search_lang_button.click()

time.sleep(3)

# 4. By.TAG_NAME - wybór po tagu HTML (np. "h1", "a", "input", itd.)
# Zwraca pierwszy napotkany tag na stronie
first_heading = driver.find_element(By.TAG_NAME, "h1")
print("Nagłówek strony:", first_heading.text)

# 5. By.LINK_TEXT - pełny tekst linku (działa dla <a>)
# Przejdźmy do linku o konkretnym tekście (jeśli istnieje na stronie)
link = driver.find_element(By.LINK_TEXT, "Talk")  # np. "Talk" w angielskiej Wiki
link.click()

# 6. By.PARTIAL_LINK_TEXT - część tekstu linku (przydatne, gdy tekst jest długi)
partial_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Privacy")
partial_link.click()

# 7. By.CSS_SELECTOR - bardzo elastyczne, jak w CSS (np. #id, .class, tag[attr=val])
# Szukamy przycisku powrotu do głównej strony w lewym górnym rogu
(może nie być widoczny na wszystkich stronach)
element = driver.find_element(By.CSS_SELECTOR, "a.mw-wiki-logo")

# 8. By.XPATH - ścieżka XML, bardzo precyzyjna, pozwala np. przechodzić po strukturze drzewa
# Przykład wyszukania pola wyszukiwania po xpath
# (poniższy przykład wymaga dopasowania, jeśli chcesz dokładny xpath konkretnego elementu)
search_input_xpath = driver.find_element(By.XPATH, '//*[@id="searchInput"]')

# Poczekaj chwilę, by zobaczyć wynik, a potem zamknij przeglądarkę
time.sleep(5)
driver.quit()
