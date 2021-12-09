# test_baidu.py

import pytest

from pages.baidu import Baidu
from utilities.data_helper import read_data_from_json_yaml, read_data_from_excel, read_data_from_pandas
from utilities.db_helper import DBHelper

# 定义要查找的sql语句
sql_string = '''select * from TestData'''

@pytest.mark.baidu
class TestBaidu:
    # @pytest.mark.parametrize('search_string, expect_string', read_data_from_json_yaml('./configs/data/baidu.yaml'))
    # @pytest.mark.parametrize('search_string, expect_string', read_data_from_json_yaml('./configs/data/baidu.json'))
    # @pytest.mark.parametrize('search_string, expect_string', read_data_from_excel(r'./configs/data/baidu.xlsx', 'baidu'))
    # 根据上述sql语句从数据库中获取测试数据并结构化返回
    @pytest.mark.parametrize('search_string, expect_string', DBHelper().db_query(sql_string))
    def test_baidu_search(self, search_string, expect_string):
        baidu = Baidu('Chrome')
        search_results = baidu.baidu_search(search_string)
        assert (expect_string in search_results) is True


if __name__ == "__main__":
    pytest.main(["-m", "baidu", "-s", "-v"])
