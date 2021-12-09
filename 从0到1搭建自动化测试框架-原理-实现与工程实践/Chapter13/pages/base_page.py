
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
