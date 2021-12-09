

import importlib
from importlib import util

import inspect
import sys
from common.data_provider import mk_test_name


class DiscoverTestCases:
    def __init__(self, test_file=None):
        self.test_file = test_file

    def find_test_module(self):
        """根据指定文件查找测试用模块并且导入它们"""
        mod_ref = []
        module_name_list = [inspect.getmodulename(self.test_file)]
        module_file_paths = [self.test_file]
        for module_name, module_file_path in zip(module_name_list, module_file_paths):
            try:
                module_spec = importlib.util.spec_from_file_location(module_name, module_file_path)
                module = importlib.util.module_from_spec(module_spec)

                module_spec.loader.exec_module(module)
                sys.modules[module_name] = module
                mod_ref.append(module)
            except ImportError:
                raise ImportError('Module: {} can not imported'.format(self.target_file_or_path))

        return mod_ref


    def find_tests(self, mod_ref):
        """遍历上一步查找到的测试模块，过滤出符合条件的测试用例"""
        test_cases = []
        for module in mod_ref:
            cls_members = inspect.getmembers(module, inspect.isfunction(module))
            for cls in cls_members:
                cls_name, cls_code_object = cls
                for func_name in dir(cls_code_object):
                    # 仅仅查找以"test"开头的测试用例
                    if func_name.startswith('test'):
                        # 获取测试类中的所有方法，并且查看是否有"__data_Provider__"属性。
                        tests_suspect = getattr(cls_code_object, func_name)
                        if hasattr(tests_suspect, "__data_Provider__"):
                            for i, v in enumerate(getattr(tests_suspect, "__data_Provider__")):
                                # 根据测试数据的组数调用mk_test_name生成新的测试用例名。
                                new_test_name = mk_test_name(tests_suspect.__name__, getattr(v, "__name__", v), i)
                                # 将测试类，原始的测试用例名，新生成的测试用例名，测试数据组成一条测试用例供测试框架后续调用。
                                test_cases.append((cls_name, tests_suspect.__name__, new_test_name, v))
                        else:
                            # 当没有"__data_Provider__"属性时，直接返回原测试用例
                            test_cases.append((cls_name, func_name, func_name, None))

        return test_cases
