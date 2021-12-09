# -*- coding: utf-8 -*-

import json
import requests


class TestLaGou:
    def setup_class(self):
        self.s = requests.Session()
        self.url = 'https://www.lagou.com'

    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        assert '拉勾' in result.text

    def test_get_new_message(self):
        # 此处需要一个方法登录获取登录的cookie，但因我们无法知道拉勾登录真实的API，故采用此方式登录
        message_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
        cookie = {
            'cookie': '_gid=GA1.2.1990476213.1617627344; gate_login_token=1846daec509ad46c6daf438a2d1934a38d0636b74ae5c735;'}
        headers = {'x-l-req-header': '{deviceType: 9}'}

        # 直接带登录态发送请求
        result = self.s.get(message_url, cookies=cookie, headers=headers)

        assert result.status_code == 200
        assert json.loads(result.content)['message'] == '成功'

    def teardown_class(self):
        self.s.close()
