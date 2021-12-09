from functools import wraps


class Test(object):
    # enabled决定使用标签挑选测试用例是否启用
    # 默认启用，如为False，则不启用
    # tag 为用户自定义标签
    def __init__(self, tag=None, enabled=True):
        self.enabled = enabled
        self.tag = tag

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        # 给原测试函数添加属性，以方便测试框架判断当前测试函数是否为测试用例
        setattr(wrapper, "__test_tag__", self.tag)
        setattr(wrapper, "__test_case_type__", "__TestCase__")
        setattr(wrapper, "__test_case_enabled__", self.enabled)
        return wrapper


class SetUpTest(object):
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        # 给原测试函数添加属性，以方便测试框架判断当前测试函数是否为测试用例的前置函数
        setattr(wrapper, "__test_case_fixture_type__", "__setUp__")
        setattr(wrapper, "__test_case_fixture_enabled__", self.enabled)
        return wrapper


class TearDownTest(object):
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        # 给原测试函数添加属性，以方便测试框架判断当前测试函数是否为测试用例的后置函数
        setattr(wrapper, "__test_case_fixture_type__", "__teardown__")
        setattr(wrapper, "__test_case_fixture_enabled__", self.enabled)
        return wrapper
