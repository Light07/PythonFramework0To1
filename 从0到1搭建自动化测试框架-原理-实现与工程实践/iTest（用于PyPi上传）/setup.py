from setuptools import setup, find_packages

setup(
    name='iTesting2',
    version='1.0.5',
    description='iTesting is a common test framework support for both UI and API test with run in parallel ability.',
    long_description='''此代码库为本人新书 **<从0到1搭建自动化测试框架：原理、实现与工程实践>** 的配套练习框架。本书基于Python编写，学习完本书，您能够完全自主开发自动化测试框架.\n
更多关于自动化测试框架的内容，请 **关注我的微信公众号iTesting** ，跟万人测试团一起成长.\n
另，对JavaScript及前端自动化测试感兴趣的同学，也可购买我的另一本书<前端自动化测试框架 -- Cypress从入门到精通>.
                                                                        --Kevin Cai（2022.01）
''',
    author='Kevin.cai',
    author_email='love.i@outlook.com',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'requests',
        'selenium'
    ],
    license='GPL',
    url='https://www.testertalk.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'iTesting2 = main:main'
        ]
    }
)
