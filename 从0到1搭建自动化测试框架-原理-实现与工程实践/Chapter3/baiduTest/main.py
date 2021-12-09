__author__ = 'iTesting'

import unittest,os
from common.html_reporter import GenerateReport


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"tests"),\
                                                pattern='*.py',top_level_dir=os.path.dirname(__file__))
    # unittest.TextTestRunner(verbosity=2).run(suite)
    html_report = GenerateReport()
    html_report.generate_report(suite)