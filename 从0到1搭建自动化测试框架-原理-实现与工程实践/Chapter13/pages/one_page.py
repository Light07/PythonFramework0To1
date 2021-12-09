import json
import time

import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.yaml_helper import YamlHelper
from configs.global_config import get_config


def cookie_to_selenium_format(cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': '', 'expires': ''}
    cookie_dict = {}
    if getattr(cookie, 'domain_initial_dot'):
        cookie_dict['domain'] = '.' + getattr(cookie, 'domain')
    else:
        cookie_dict['domain'] = getattr(cookie, 'domain')
    for k in list(cookie_selenium_mapping.keys()):
        key = k
        value = getattr(cookie, k)
        cookie_dict[key] = value
    return cookie_dict


class OnePage(BasePage):
    # 从全局变量中获取DOMAIN
    DOMAIN = get_config('config')["one_home_page"]
    URI = get_config('config')["one_login_uri"]
    HEADER = get_config('config')["one_header"]

    # yaml文件相对于本文件的文件路径
    element_locator_yaml = './configs/element_locator/one_page.yaml'
    element = YamlHelper.read_yaml(element_locator_yaml)

    # 获取页面项目对象VIPTEST
    Project = (By.XPATH, element["PROJECT_NAME"])

    def __init__(self, driver=None):
        super().__init__(driver)
        self.s = requests.Session()
        self.login_url = self.URI
        self.home_page = self.DOMAIN
        self.header = self.HEADER

    def login_and_set_cookie(self, login_data):
        result = self.s.post(self.login_url, data=json.dumps(login_data), headers=self.header)
        # 断言登录成功
        assert result.status_code == 200
        assert json.loads(result.text)["user"]["email"].lower() == login_data["email"]

        # 根据实际情况解析cookies，此处需结合实际业务场景
        all_cookies = self.s.cookies._cookies[".ones.ai"]["/"]

        # 删除所有cookies
        self.driver.get(self.home_page)
        self.driver.delete_all_cookies()

        # 把接口登录后的cookie传递给Selenium/WebDriver，传递登录状态
        for k, v in all_cookies.items():
            self.driver.add_cookie(cookie_to_selenium_format(v))

        return self.driver

    def find_project_name(self):
        self.driver.get(self.home_page)
        # 此处硬编码，等页面加载完毕
        time.sleep(3)
        return self.driver.find_element(*self.Project).get_attribute('innerHTML')

