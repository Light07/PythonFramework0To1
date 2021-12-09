import argparse
import sys
import shlex
import os


def parse_options(user_options=None):
    parser = argparse.ArgumentParser(prog='iTesting', description="iTesting framework demo")
    parser.add_argument("-t", action="store", default="." + os.sep + 'tests', dest="test_targets", metavar='target run path/file',
                        help="Specify run path/file")
    include_tag = parser.add_mutually_exclusive_group()
    include_tag.add_argument("-i", action="store", default=None, dest="include_tags_any_match", metavar="user provided tags(Any)",
                             help="Specify tags to run")
    include_tag.add_argument("-ai", action="store", default=None, dest="include_tags_full_match", metavar="user provided tags(Full Match)",
                             help="Specify tags to run, full match")

    exclude_tags = parser.add_mutually_exclusive_group()
    exclude_tags.add_argument("-e", action="store", default=None, dest="exclude_tags_any_match", metavar="user exclude tags(Any)",
                              help="Exclude tags to run")

    exclude_tags.add_argument("-ae", action="store", default=None, dest="exclude_tags_full_match", metavar="user exclude tags(Full Match)",
                              help="Exclude tags to run, full match")

    all_include_tag = parser.add_mutually_exclusive_group()
    all_include_tag.add_argument("-I", action="store", default=None, dest="include_groups_any_match", metavar="user provided class tags(Any)",
                                 help="Specify class to run")

    all_exclude_tag = parser.add_mutually_exclusive_group()
    all_exclude_tag.add_argument("-E", action="store", default=None, dest="exclude_groups_any_match", metavar="user exclude class tags(Any)",

                                 help="Exclude class to run")

    if not user_options:
        args = sys.argv[1:]

    else:

        args = shlex.split(user_options)
    options, un_known = parser.parse_known_args(args)

    return os.path.abspath(options.test_targets)


def main(args=None):
    return parse_options(args)


if __name__ == "__main__":
    print(main())
