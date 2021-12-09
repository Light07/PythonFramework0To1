from common.data_provider import data_provider


class DemoTest:

    @data_provider([('iTesting',), ('kevin',)])
    def test_demo_data_driven(self, data):
        """Demo 演示"""
        print(55)
        print(data)
