# -*- coding: utf-8 -*-
from common.test_case_finder import DiscoverTestCases

if __name__ == "__main__":
    test_file_path = r"D:\pythonProject\Chapter6\tests\test_demo.py"
    case_finder = DiscoverTestCases(test_file_path)
    test_module = case_finder.find_test_module()
    print(test_module)
    test_cases = case_finder.find_tests(test_module)
    print(88)
    print(test_cases)