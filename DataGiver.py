import cloudscraper

def fetch_data_with_cloudscraper():
    url = "https://www.spaceweatherlive.com/ru/arhiv/2024/11/15/dayobs.html"

    # Создаем объект CloudScraper
    scraper = cloudscraper.create_scraper(browser={
        "browser": "chrome",
        "platform": "windows",
        "mobile": False
    })

    try:
        response = scraper.get(url, timeout=10)

        if response.status_code == 200:
            print("Данные успешно получены!")
            with open("output.html", "w", encoding="utf-8") as file:
                file.write(response.text)
            return response.text
        else:
            print(f"Ошибка доступа, код: {response.status_code}")
            print(f"Тело ответа: {response.text}")
            return None

    except Exception as e:
        print(f"Ошибка: {e}")
        return None


# Вызов функции
fetch_data_with_cloudscraper()
