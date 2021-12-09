# coding=utf-8

from selenium import webdriver
import unittest
import time


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("iTesting")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        search_results = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute('innerHTML')
        self.assertEqual('iTesting' in search_results, True)

    def tearDown(self):
        self.driver.quit()

#
# if __name__ == "__main__":
#     unittest.main(verbosity=2)