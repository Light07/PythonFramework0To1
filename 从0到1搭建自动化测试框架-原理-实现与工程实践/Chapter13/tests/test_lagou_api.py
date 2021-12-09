# -*- coding: utf-8 -*-

import requests

from common.test_decorator import SetUpTest, TearDownTest, Test
from configs.global_config import get_config


class TestLaGou:
    test_case_id = 'Jira-1023'

    @SetUpTest()
    def set_up(self):
        self.s = requests.Session()
        # 获取环境变量中lagou的url并赋予self.url
        self.url = get_config('config')["Lagou_url"]

    @Test(tag='smoke1')
    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        assert '拉勾' in result.text

    @TearDownTest()
    def clean_up(self):
        self.s.close()
