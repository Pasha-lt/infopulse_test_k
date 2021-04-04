from hw_3_4 import *
import pytest


@pytest.mark.parametrize('list_number, expected_result', [
    pytest.param(([2, 3, 5, 5, 6, 6, 7, 7, 7, 8, 9, 0]), (3), id='my example test_hw_3_4'),
    pytest.param(([1, 1, 1, 1, 1, 0]), (5), id='my example test_hw_3_4')
])
def test_hw_3_4_4(list_number, expected_result):
    res = hw_3_4_4(list_number)
    assert res == expected_result
