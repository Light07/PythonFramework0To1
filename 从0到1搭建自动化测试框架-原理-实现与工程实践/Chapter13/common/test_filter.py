import re


class TestFilter:
    def __init__(self, test_suites):
        self.suites = test_suites
        # 添加一个被忽略的测试用例集
        self.exclude_suites = None

    # 标签筛选策略，只要包括，即运行。
    def filter_tags_in_any(self, user_option_tags):
        """只要包括某个标签，即运行"""

        included_cls = []
        remain_cases = []
        # 将被忽略的测试用例添加到excluded_cases列表
        excluded_cases = []

        for i in self.suites:
            tags_in_class = i[0]
            tags = []

            def recursion(raw_tag):
                if raw_tag:
                    if isinstance(raw_tag, (list, tuple)):
                        for item in raw_tag:
                            if isinstance(item, (list, tuple)):
                                recursion(item)
                            else:
                                tags.append(item)
                    else:
                        return re.split(r'[;,\s]\s*', raw_tag)
                return tags

            after_parse = recursion(tags_in_class)

            if any(map(lambda x: True if x in after_parse else False, user_option_tags)):
                included_cls.append(i[0])

        # 判断，如果在待测试用例中，则放入待测试用例列表，否则放入excluded_cases列表。
        for s in self.suites:
            if s[0] in set(included_cls):
                remain_cases.append(s)
            else:
                excluded_cases.append(s)

        self.suites = remain_cases
        self.exclude_suites = excluded_cases

    # 根据标签，依据不同的标签筛选策略进行测试用例筛选
    def tag_filter_run(self, in_any_tags):
        if in_any_tags:
            self.filter_tags_in_any(in_any_tags)
        # 同时返回待运行的测试用例集，以及被忽略的测试用例集
        return self.suites, self.exclude_suites
