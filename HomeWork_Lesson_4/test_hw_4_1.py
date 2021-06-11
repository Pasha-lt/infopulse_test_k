from hw_4_1 import *
import pytest



# Вариант с вынесением тестовых значений из декоратора.
parametrizes = [
    (3, 'one','3one'),
    ('new word', 79.90,'new word79.9'),
    ('0', '0',0.0),
    (5, 5, 10.0),
]
@pytest.mark.parametrize('variable_a, variable_b, expected_result', parametrizes)
def test_hw_4_1(variable_a, variable_b, expected_result):
    res = hw_4_1_1(variable_a, variable_b)
    assert res == expected_result



# @pytest.mark.parametrize('variables, expected_result',[
#     pytest.param(([3, 'one']),('3one'), id='first - int, second - str'),
#     pytest.param((['new word', 79.90]),('new word79.9'), id='first - str, second - float'),
#     pytest.param((['0', '0']),(0.0), id='first - zero, second - zero'),
#     pytest.param(([5, 5]),(10.0), id='first - int, second - int'),
# ])
# def test_hw_4_1(variables, expected_result):
#     variable_a, variable_b = variables
#     res = hw_4_1_1(variable_a, variable_b)
#     assert res == expected_result

