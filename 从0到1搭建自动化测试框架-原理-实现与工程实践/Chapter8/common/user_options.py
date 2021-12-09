import argparse
import importlib.util
import sys
import shlex
import os


def parse_options(user_options=None):
    parser = argparse.ArgumentParser(prog='iTesting', description='iTesting framework demo')
    parser.add_argument('-env', action='store', default='qa', dest='default_env', metavar='target environment',
                        choices=['qa', 'prod'], help='Specify test environment')
    parser.add_argument('-t', action='store', default='.' + os.sep + 'tests', dest='test_targets',
                        metavar='target run path/file',
                        help='Specify run path/file')

    if not user_options:
        args = sys.argv[1:]
    else:
        args = shlex.split(user_options)

    options, un_known = parser.parse_known_args(args)

    if options.test_targets:
        if not os.path.isdir(options.test_targets) and not os.path.isfile(options.test_targets):
            parser.error("Test targets must either be a folder path or a file path, it either be absolute path \
                         or relative path, if it is relative , it must relative to tests folder under your root folder")
        if not os.path.isabs(options.test_targets):
            options.test_targets = os.path.abspath(options.test_targets)
        else:
            options.test_targets = options.test_targets

    if options.default_env:
        try:
            module_package = '.' + os.sep + 'configs' + os.sep + 'test_env'
            module_name = module_package + os.sep + '{}_env'.format(options.default_env)
            module_file = '{}.py'.format(module_name)
            module_spec = importlib.util.spec_from_file_location(module_name, module_file)
            env = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(env)
            options.config = {item: getattr(env, item, None) for item in dir(env) if not item.startswith("__")}
        except ImportError:
            raise ImportError('Module: {} can not imported'.format(module_name))

    return options
