# Repozytorium do prezentacji na lekcję Aplikacji Desktopowych - Python.
`app.py` - zawiera intrukcje z części "PIerwszy skrypt scrapingowy" <br>
`methods.py` - zawiera metody "łapania" elementów + przykładowy kod <br>
`bonus.py` - zawiera pełnoprawny program wykorzystujący bilbiotekę selenium <br>


##  Wymagania wstępne

- Python 3.x zainstalowany (sprawdź: `python --version`)
- `pip` zainstalowany (sprawdź: `pip --version`)
- Przeglądarka Chrome i/lub Firefox zainstalowana



##  Instalacja Selenium

```bash
pip install selenium
````



##  Konfiguracja dla Google Chrome

### 1.  Zainstaluj Chrome

Pobierz ze strony: [https://www.google.com/chrome/](https://www.google.com/chrome/)

### 2.  Pobierz ChromeDriver

1. Sprawdź wersję swojej przeglądarki Chrome:
   Wejdź na `chrome://settings/help`
   np. `Version 124.0.6367.91`

2. Wejdź na stronę:
   [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

3. Pobierz wersję ChromeDriver odpowiadającą twojej wersji przeglądarki

4. Wypakuj plik `chromedriver.exe` do folderu projektu lub np. `C:\WebDriver\bin\`

### 3.  Przykład kodu dla Chrome

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('chromedriver.exe')  # lub pełna ścieżka np. 'C:/WebDriver/bin/chromedriver.exe'
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')
time.sleep(2)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('OpenAI')
search_box.submit()

time.sleep(10)
driver.quit()
```



## 🦊 Konfiguracja dla Mozilla Firefox

### 1. Zainstaluj Firefox

Pobierz ze strony: [https://www.mozilla.org/firefox/new/](https://www.mozilla.org/firefox/new/)

### 2.  Pobierz GeckoDriver

1. Wejdź na stronę:
   [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

2. Pobierz wersję `geckodriver-vX.X.X-win64.zip`

3. Wypakuj plik `geckodriver.exe` do folderu projektu lub np. `C:\WebDriver\bin\`

### 3.  Przykład kodu dla Firefox

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Upewnij się, że ścieżka jest poprawna

service = Service('geckodriver.exe')  # lub pełna ścieżka
driver = webdriver.Firefox(service=service, options=options)

driver.get('https://www.google.com')
time.sleep(2)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('OpenAI')
search_box.submit()

time.sleep(10)
driver.quit()
```

> ℹJeśli używasz Firefoksa w wersji portable lub zainstalowanego poza domyślną ścieżką, musisz **ręcznie podać lokalizację `firefox.exe`**.



## Uwagi końcowe

* WebDriver musi pasować do wersji przeglądarki.
* Plik `chromedriver.exe`/`geckodriver.exe` musi być w katalogu projektu lub dodany do zmiennej środowiskowej PATH.
* Na systemach 64-bitowych Firefox może być w `Program Files` lub `Program Files (x86)` – sprawdź dokładnie.

