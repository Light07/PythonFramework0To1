import os

from common.test_case_finder import DiscoverTestCases
from common.user_options import parse_options
from configs.global_config import init, set_config
from tests.test_baidu import DemoTest


def main(args=None):
    options = parse_options(args)
    print(444)
    print(options.test_targets)
    print(options.config)
    init()
    print(1234)
    set_config('config', options.config)
    test_case = options.test_targets + os.sep + 'test_baidu.py'
    # 生成DiscoverTestCases类实例
    case_finder = DiscoverTestCases(test_case)
    # 查找测试模块并导入
    test_module = case_finder.find_test_module()
    # 查找测试用例
    test_cases = case_finder.find_tests(test_module)
    for i in test_cases:
        print(i)

    demo = DemoTest()
    demo.test_demo_data_driven(('iTesting',))


if __name__ == "__main__":
    main()
