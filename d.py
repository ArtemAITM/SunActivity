from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def fetch_data_with_selenium():
    url = "https://www.spaceweatherlive.com/ru/arhiv/2024/11/01/dayobs.html"
    xpath_expression = "/html/body/div[2]/div/div/div[1]/div[6]/table/tbody/tr/td[1]/span[1]"

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Фоновый режим
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_expression))
        )
        result = element.text.strip()
        print(f"Extracted data: {result}")

        # Сохранение данных
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(result)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()


# Вызов функции
fetch_data_with_selenium()
