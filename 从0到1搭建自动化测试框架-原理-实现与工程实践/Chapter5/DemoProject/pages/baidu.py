import time


from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.yaml_helper import YamlHelper


class Baidu(BasePage):
    BASE_URL = "http://www.baidu.com/"

    element_locator_yaml = './configs/yamls/en/baidu.yaml'
    element = YamlHelper.read_yaml(element_locator_yaml)

    input_box = (By.ID, element["KEY_WORLD_LOCATOR"])
    search_btn = (By.ID, element["SEARCH_BUTTON_LOCATOR"])
    first_result = (By.XPATH, element["FIRST_RESULT_LOCATOR"])

    def __init__(self, driver):
        super().__init__(driver)

    def baidu_search(self, search_string):
        self.driver.get(self.BASE_URL)
        self.driver.find_element(*self.input_box).clear()
        self.driver.find_element(*self.input_box).send_keys(search_string)
        self.driver.find_element(*self.search_btn).click()
        time.sleep(2)
        search_results = self.driver.find_element(*self.first_result).get_attribute('innerHTML')
        return search_results
