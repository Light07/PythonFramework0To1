from common.data_provider import data_provider
from common.test_decorator import Test
from configs.global_config import get_config


class DemoTest:

    @data_provider([('iTesting', ), ('123',)])
    # 给测试方法添加tag标签，指定其tag值为smoke
    @Test(tag='smoke')
    def test_demo_data_driven(self, data):
        """Demo 演示"""
        print(data)
        print(get_config('config'))
