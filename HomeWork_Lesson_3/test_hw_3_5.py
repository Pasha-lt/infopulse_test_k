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

text_result2 = ['are', 'are', 'are', 'at', 'bebut', 'befootball', 'bewe', 'coach', 'least', 'need', 'not', 'not',
                'notwhat', 'should', 'to', 'to', 'used', 'we', 'we', 'we', 'we', 'we', 'what', 'what']

dict_result = {'we': 5, 'are': 3, 'notwhat': 1, 'should': 1, 'bewe': 1, 'not': 2, 'what': 2, 'need': 1, 'to': 2,
               'bebut': 1, 'at': 1,
               'least': 1, 'used': 1, 'befootball': 1, 'coach': 1}


@pytest.mark.parametrize('text, expected_result', [
    pytest.param((text), (28), id='basic example'),
    pytest.param((''), (0), id='zero'),
    pytest.param(('two words'), (2), id='my example'),
])
def test_hw_3_5_1(text, expected_result):
    res = hw_3_5_1(text)
    assert res == expected_result


@pytest.mark.parametrize('text, text_result', [
    pytest.param((text), (text_result), id='basic test function 3_5_2')
])
def test_hw_3_5_2(text, text_result):
    res = hw_3_5_2(text)
    assert res == text_result


@pytest.mark.parametrize('text, text_result2', [
    pytest.param((text), (text_result2), id='basic test function hw_3_5_3')])
def test_hw_3_5_3(text, text_result2):
    res = hw_3_5_3(text)
    assert res == text_result2


@pytest.mark.parametrize('text, dict_result', [
    pytest.param((text), (dict_result), id='basic test hw_3_5_4')
])
def test_hw_3_5_4(text, dict_result):
    res = hw_3_5_4(text)
    assert res == dict_result
