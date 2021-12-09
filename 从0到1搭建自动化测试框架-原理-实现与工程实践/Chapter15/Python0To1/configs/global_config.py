def init():
    global _config
    _config = {}


def get_config(k):
    try:
        return _config[k]
    except KeyError:
        return None


def set_config(k, v):
    try:
        _config[k] = v
    except KeyError:
        return None
