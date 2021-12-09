# -*- coding: utf-8 -*-

from common.data_provider import data_provider
from common.test_decorator import TearDownTest, SetUpTest, Test
from pages.one_page import OnePage


class TestOneAI:
    # 直接通过接口调用的方式登录，首先进行初始化
    def __init__(self):
        self.one_page = OnePage()

    @SetUpTest()
    def setup_method(self):
        # 请读者自行注册账户进行测试
        self.one_page.login_and_set_cookie({"password": "P@ssw0rd", "email": "Follow_iTesting@outlook.com"})

    @data_provider([("VIPTEST",)])
    # 给测试方法添加tag标签，指定其tag值为smoke
    @Test(tag='smoke')
    def verify_project_name(self, project_name):
        # 再次访问目标页面，此时登录状态已经传递过来了
        element = self.one_page.find_project_name()
        # 断言项目VIPTEST存在
        assert element == project_name

    # 测试后的清理
    @TearDownTest()
    def teardown_method(self):
        self.one_page.driver.close()
        self.one_page.s.close()
