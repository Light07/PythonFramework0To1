# -*- coding: utf-8 -*-

from common.test_case_finder import DiscoverTestCases

if __name__ == "__main__":
    # 测试文件笔者暂时硬编码。
    # 在后续的章节中笔者将演示如何自动化获取测试文件。
    # test_file_path = r"D:\pythonProject\Chapter6\tests\test_demo.py"
    test_file_path = r"/Users/laternbright/projects/pythonProject/tests/test_demo.py"

    # 生成DiscoverTestCases类实例
    case_finder = DiscoverTestCases(test_file_path)
    # 查找测试模块并导入
    test_module = case_finder.find_test_module()
    # 查找测试用例
    test_cases = case_finder.find_tests(test_module)
    for i in test_cases:
        print(i)
