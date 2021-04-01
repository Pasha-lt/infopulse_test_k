import pytest
from hw_3_5 import *

text = \
    """
    We are not  what we should be!
    We are not what we need to be.
    But at least we are not what we used to be
    (Football Coach)
    """

text_result = \
    """
    We are not  what we should be
    We are not what we need to be
    But at least we are not what we used to be
    (Football Coach)
    """


@pytest.mark.parametrize('text , text_result', [
    pytest.param((text), (text_result), id='test function 3_5_2')
])
def test_hw_3_5_2(text, text_result):
    res = hw_3_5_2(text)
    assert res == text_result


@pytest.mark.parametrize('text, expected_result', [
    pytest.param((text), (28), id='basic example'),
    pytest.param((''), (0), id='zero'),
    pytest.param(('two words'), (2), id='my example'),
])
def test_hw_3_5_1(text, expected_result):
    res = hw_3_5_1(text)
    assert res == expected_result
