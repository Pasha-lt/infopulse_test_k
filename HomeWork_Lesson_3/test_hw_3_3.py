from hw_3_3 import *
import pytest


@pytest.mark.parametrize("number_a, expected_result", [
    pytest.param((8), (1, 3), id='my example test_hw_3_3'),
    pytest.param((13), (13, 0), id='my example2 test_hw_3_3')
])
def test_hw_3_3_3(number_a, expected_result):
    res = hw_3_3_3(number_a)
    assert res == expected_result
