import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.yaml_helper import YamlHelper
from configs.global_config import get_config


class Baidu(BasePage):
    # 从全局变量中获取DOMAIN
    DOMAIN = get_config('config')["DOMAIN"]

    # yaml文件相对于本文件的文件路径
    element_locator_yaml = './configs/element_locator/baidu.yaml'
    element = YamlHelper.read_yaml(element_locator_yaml)

    # 获取所有的页面对象
    input_box = (By.ID, element["KEY_WORLD_LOCATOR"])
    search_btn = (By.ID, element["SEARCH_BUTTON_LOCATOR"])
    first_result = (By.XPATH, element["FIRST_RESULT_LOCATOR"])

    def __init__(self, driver=None):
        super().__init__(driver)

    # 定义类方法
    def baidu_search(self, search_string):
        self.driver.get(self.DOMAIN)
        self.driver.find_element(*self.input_box).clear()
        self.driver.find_element(*self.input_box).send_keys(search_string)
        self.driver.find_element(*self.search_btn).click()
        time.sleep(2)
        search_results = self.driver.find_element(*self.first_result).get_attribute('innerHTML')
        return search_results
