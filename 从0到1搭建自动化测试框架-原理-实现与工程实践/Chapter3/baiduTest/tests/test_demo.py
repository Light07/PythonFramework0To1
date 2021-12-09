import pytest


@pytest.fixture(params=['hello', 'iTesting'], autouse=True, ids=['test1', 'test2'], name='test')
def my_method(request):
    print(request.param)


def test_use_fixtures_01():
    print('\n this is the 1st test')


def test_use_fixtures_02():
    print('\n this is the 2nd test')