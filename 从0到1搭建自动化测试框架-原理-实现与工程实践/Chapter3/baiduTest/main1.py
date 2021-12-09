# -*- coding: utf-8 -*-

import pytest
import os
import glob


# 查找所以待执行的测试用例module，见《04|必知必会，打好Python基本功》
def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)
    md = glob.glob(os.path.join(absolute_f, "*.py"))
    return [f for f in md if os.path.isfile(f) and not f.endswith('__init__.py')]


if __name__ == "__main__":
    # 得出测试文件夹地址
    test_folder = os.path.join(os.path.dirname(__file__), 'tests')
    # 得出测试文件夹下的所有测试用例
    target_file = find_modules_from_folder(test_folder)
    # 直接运行所有的测试用例
    pytest.main([*target_file, '-v'])