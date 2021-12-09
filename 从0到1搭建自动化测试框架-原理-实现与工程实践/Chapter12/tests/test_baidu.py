from selenium import webdriver

from common.data_provider import data_provider
from common.test_decorator import Test
from pages.baidu import Baidu
from common.my_logger import MyLogger

log = MyLogger().get_logger(__name__)


class BaiduTest:

    @data_provider(
        [('iTesting', 'iTesting'), ('helloqa.com', 'iTesting')])
    # 给测试方法添加tag标签，指定其tag值为smoke
    @Test(tag='smoke')
    def test_baidu_search(self, *data):
        # 启动浏览器，指定运行的机器为Win10， 浏览器为Chrome
        # self.driver = webdriver.Remote(
        #     command_executor='http://192.168.0.109:4444/wd/hub',
        #     desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True, 'platformName': 'Win10'})

        # 初始化Page对象Baidu
        # 使用Selenium Grid指定的Driver，并且指派运行的机器和浏览器
        # baidu = Baidu(self.driver)

        # 如果要本地运行，可以注释掉上面的代码
        # 并打开下面一行的注释
        baidu = Baidu()

        # 测试用例中调用类方法，并断言,
        search_string, expect_string = data
        # log.debug("BaiduTest.test_baidu_search开始测试，输入参数是 - {input}， 期望结果包含 - {output}".format(input=search_string, output=expect_string))

        results = baidu.baidu_search(search_string)
        assert expect_string in results

        # 关闭浏览器
        baidu.close()
