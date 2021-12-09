from common.data_provider import data_provider


class TestDemo():
    @data_provider(['iTesting', 'Kevin'])
    def test_demo_data_driven(self, data):
        """Demo 演示"""
        print(data)
