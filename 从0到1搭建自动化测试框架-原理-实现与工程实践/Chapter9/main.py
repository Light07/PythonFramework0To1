from collections import OrderedDict

from common.test_case_finder import DiscoverTestCases
from common.test_filter import TestFilter
from common.user_options import parse_options
from configs.global_config import init, set_config


def group_test_cases_by_class(cases_to_run):
    test_groups_dict = OrderedDict()
    for item in cases_to_run:
        tag_filter, cls, func_name, func, value = item
        test_groups_dict.setdefault(cls, []).append((tag_filter, cls, func_name, func, value))
    test_groups = [(x, y) for x, y in zip(test_groups_dict.keys(), test_groups_dict.values())]
    return test_groups


def main(args=None):
    # 解析用户输入
    options = parse_options(args)
    # 初始化全局变量
    init()
    # 设置全局环境变量
    set_config('config', options.config)

    # 从默认文件夹tests开始查找测试用例
    case_finder = DiscoverTestCases()
    # 查找测试模块并导入
    test_module = case_finder.find_test_module()
    # 查找并筛选测试用例
    original_test_cases = case_finder.find_tests(test_module)
    # 根据用户输入参数-i进一步筛选
    raw_test_suites = TestFilter(original_test_cases).tag_filter_run(options.include_tags_any_match)
    # 获取到最终的测试用例集，并按class名组织
    test_suites = group_test_cases_by_class(raw_test_suites)

    # 运行每一个测试用例
    for test_suite in test_suites:
        test_class, func_run_pack_list = test_suite
        for func_run_pack in func_run_pack_list:
            cls_group__name, cls, func_name, func, value = func_run_pack
            cls_instance = cls()
            if value:
                getattr(cls_instance, func.__name__).__wrapped__(cls_instance, *value)
            else:
                getattr(cls_instance, func.__name__).__wrapped__(cls_instance)


if __name__ == "__main__":
    main("-env prod -i sanity -t ./tests")
