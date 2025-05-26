import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def main():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    service = Service("geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("https://www.wikipedia.org/")
        time.sleep(2)

        search_input = driver.find_element(By.ID, "searchInput")
        search_input.send_keys("Selenium (software)")
        search_button = driver.find_element(By.CLASS_NAME, "pure-button-primary-progressive")
        search_button.click()

        time.sleep(3)

        heading = driver.find_element(By.ID, "firstHeading")
        text = heading.text

        with open("wynik.txt", "w", encoding="utf-8") as f:
            f.write(f"Tytuł strony: {text}")

        print("Zapisano wynik do pliku wynik.txt.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    main()
