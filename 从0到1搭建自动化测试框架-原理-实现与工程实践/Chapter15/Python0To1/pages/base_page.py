
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        if driver:
            self.driver = driver
        else:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-setuid-sandbox")
            self.driver = webdriver.Chrome(chrome_options=options)

    def open_page(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
