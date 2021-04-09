import pytest
from hw_4_2 import *


@pytest.mark.parametrize('year, expected_result', [
    pytest.param((2000), (True), id='2000 True'),
    pytest.param((500), (False), id='500 False'),
    pytest.param((2001), (False), id='2001 False'),
    pytest.param((804), (True), id='804 True'),
    pytest.param((800), (True), id='800 True'),
])
def test_hw_4_2_1(year, expected_result):
    res = is_year_leap(year)
    assert res == expected_result


# Распаковываем sides отдельно плюс одна строчка.
@pytest.mark.parametrize('sides, expected_result', [
    pytest.param((3, 4, 5), (True), id='3,4,5 - rectangle exist'),
    pytest.param((0, 4, 0), (False), id='0,4,0 - rectangle not exist'),
    pytest.param((1, 1, 3), (False), id='1,1,3 - rectangle not exist'),
])
def test_hw_4_2_2(sides, expected_result):
    side_a, side_b, side_c = sides
    res = triangle(side_a, side_b, side_c)
    assert res == expected_result


# Вместо разпаковки передаем по индексу.
@pytest.mark.parametrize('sides, expected_result', [
    pytest.param((3, 4, 5), ('Versatile triangle'), id='3,4,5 - Versatile triangle'),
    pytest.param((0, 4, 0), ('Not a tringle'), id='0,4,0 - Not a triangle'),
    pytest.param((2, 3, 2), ('Isosceles triangle'), id='2,3,2 - Isosceles triangle'),
    pytest.param((2, 2, 3), ('Isosceles triangle'), id='2,2,3 - Isosceles triangle'),
    pytest.param((3, 2, 2), ('Isosceles triangle'), id='3,2,2 - Isosceles triangle'),
    pytest.param((3, 3, 3), ('Equilateral triangle'), id='3,3,3 - Equilateral triangle'),
    pytest.param((6, 18, 21), ('Versatile triangle'), id='6,18,21 - Versatile triangle'),
])
def test_hw_4_2_3(sides, expected_result):
    res = hw_4_2_3(sides[0], sides[1], sides[2])
    assert res == expected_result


@pytest.mark.parametrize('coords, extual_result', [
    pytest.param((4, 4, 4, 4), ('Растояние между x2 и x1: 0. Растояние между y2 и y1: 0'), id='4,4,4,4 = 0,0 '),
    pytest.param((-4, 4, -6, -10), ('Растояние между x2 и x1: 2. Растояние между y2 и y1: 14'), id='-4,4,-6,-10 = 0,0 ')
])
def test_hw_4_2_3(coords, extual_result):
    x1, y1, x2, y2 = coords
    res = distance(x1, y1, x2, y2)
    assert res == extual_result
