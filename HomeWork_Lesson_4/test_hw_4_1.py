from hw_4_1 import *
import pytest

@pytest.mark.parametrize('variables, expected_result',[
    pytest.param(([3, 'one']),('3one'), id='first - int, second - str'),
    pytest.param((['new word', 79.90]),('new word79.9'), id='first - str, second - float'),
    pytest.param((['0', '0']),(0.0), id='first - zero, second - zero'),
    pytest.param(([5, 5]),(10.0), id='first - int, second - int'),
])
def test_hw_4_1(variables, expected_result):
    variable_a, variable_b = variables
    res = hw_4_1_1(variable_a, variable_b)
    assert res == expected_result
