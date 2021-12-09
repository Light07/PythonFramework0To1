from common.data_provider import data_provider
from configs.global_config import get_config

class DemoTest:

    @data_provider([('iTesting',), ('kevin',)])
    def test_demo_data_driven(self, data):
        """Demo 演示"""
        print(data)
        print(get_config('config'))