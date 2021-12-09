__author__ = 'iTesting'

# -*-coding=utf-8 -*-
import os
import re


class Test(object):
    def __init__(self):
        self.test_base = os.path.dirname(__file__)
        # 获取tests文件夹所在路径
        self.test_dir = os.path.join(self.test_base, 'tests')
        # 列出所有待测试文件
        self.test_list = os.listdir(self.test_dir)
        print(self.test_list)
        # 定义正则匹配规则，过滤__init__.py和 *.pyc文件
        self.pattern = re.compile(r'(__init__.py|.*.pyc)')

         # 测试结果写文件
        if not os.path.exists(os.path.join(self.test_base,"log.txt")):
            f = open(os.path.join(self.test_base,"log.txt"),'a')
        else:
            f = open(os.path.join(self.test_base,"log.txt"),'w')
            f.flush()
        f.close()

    # 运行符合要求的测试文件并写入log.txt
    def run_test(self):
        for py_file in self.test_list:
            match = self.pattern.match(py_file)
            if not match:
                print(py_file)
                print(os.path.join(self.test_dir,py_file),os.path.join(self.test_base,"log.txt"))
                os.system('python %s 1>>%s 2>&1' %(os.path.join(self.test_dir,py_file),os.path.join(self.test_base,"log.txt")))


if __name__ == "__main__":
    test = Test()
    test.run_test()