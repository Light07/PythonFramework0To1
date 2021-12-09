import re


def data_provider(test_data):
    def wrapper(func):
        setattr(func, "__data_Provider__", test_data)
        global index_len
        index_len = len(str(len(test_data)))
        return func
    return wrapper


def mk_test_name(name, value, index=0):
    index = "{0:0{1}d}".format(index + 1, index_len)
    test_name = "{0}_{1}_{2}".format(name, index, str(value))
    return re.sub(r'\W|^(?=\d)', '_', test_name)