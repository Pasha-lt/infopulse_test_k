from hw_3_2 import *
import pytest


@pytest.mark.parametrize("string_a, expected_result", [
    pytest.param(('iofu'), ('fuio')),
    pytest.param(('Pasha'), ('haPas')),
])
def test_hw_3_2(string_a, expected_result):
    res = hw_3_2(string_a)
    assert res == expected_result
