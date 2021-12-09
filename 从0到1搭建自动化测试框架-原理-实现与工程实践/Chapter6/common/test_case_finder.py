import importlib
from importlib import util

import inspect
import sys
from common.data_provider import mk_test_name


class DiscoverTestCases:
    def __init__(self, test_file=None):
        self.test_file = test_file

    def find_test_module(self):
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
        test_cases = []
        for module in mod_ref:
            cls_members = inspect.getmembers(module, inspect.isfunction)
            for cls in cls_members:
                cls_name, cls_code_object = cls
                for func_name in dir(cls_code_object):
                    tests_suspect = getattr(cls_code_object, func_name)
                    print(333, tests_suspect)
                    if hasattr(tests_suspect, "__data_Provider__"):
                        for i, v in enumerate(getattr(tests_suspect, "__data_Provider__")):
                            new_test_name = mk_test_name(tests_suspect.__name__, getattr(v, "__name__", v), i)
                            # cls_code_object() is the test class eg: <class 'test_page_add.TestSumData3'>
                            # test_cases.append((cls_code_object(), func_name, new_test_name, v))
                    else:
                        test_cases.append((cls_code_object(), func_name, func_name, None))

        return test_cases
