import re
from functools import wraps

def data_provider(test_data):
    def wrapper(func):
        print(4)
        print(func.__name__)
        setattr(func, "__data_Provider__", test_data)
        global index_len
        index_len = len(str(len(test_data)))
        print(dir(func))

    return wrapper


def mk_test_name(name, value, index=0):
    index = "{0:0{1}}".format(index+1, index_len)
    test_name = "{0}_{1}_{2}".format(name, index, value)
    return re.sub(r'\W|^(?=\d)', '_', test_name).rstrip('_')