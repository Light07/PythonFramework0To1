from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        if str(driver).capitalize() == "Chrome":
            self.driver = webdriver.Chrome()
        elif str(driver).capitalize() == "Firefox":
            self.driver = webdriver.Firefox()
        elif str(driver).capitalize() == "Safari":
            self.driver = webdriver.Safari()
        else:
            self.driver = webdriver.Chrome()

    def open_page(self, url):
        self.driver.get(url)