from functools import wraps


class Test(object):
    def __init__(self, enabled=True):
        self.enabled = enabled

    def __call__(self, func):
        @wraps(func)
        def wrapper():
            return func

        setattr(wrapper, "__test_case_type__", "__TestCase__")
        setattr(wrapper, "__test_case_enabled__", self.enabled)
        return wrapper
