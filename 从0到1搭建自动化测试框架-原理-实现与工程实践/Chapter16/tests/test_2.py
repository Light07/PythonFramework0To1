from common.test_decorator import Test
from common.my_logger import MyLogger

log = MyLogger().get_logger(__name__)


class WrongCases:
    test_case_id = 'Jira-1025'

    # 给测试方法添加tag标签，指定其tag值为smoke
    @Test(tag='smoke')
    def test_assert_error(self):
        self.test_case_id = 'Jira-1026'
        log.error("Assert Error")
        assert 1 == 2

    @Test(tag='not-run')
    def test_not_run(self):
        self.test_case_id = 'Jira-1027'
        log.info("Not run")
        assert 1 == 1

    @Test(tag='smoke')
    def test_unknown_error(self):
        self.test_case_id = 'Jira-1028'
        raise ValueError("User Error")
