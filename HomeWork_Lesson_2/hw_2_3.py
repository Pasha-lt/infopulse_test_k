def hw_2_3_1(list_a):
    """the function that output the third from the end element"""
    return list_a[-3]


def hw_2_3_2(list_a):
    """the function that output the first letter of the second word from the list"""
    return list_a[1][0]


def hw_2_3_3(list_a):
    """the function that output the last letter of the last word"""
    return list_a[-1][-1]


def hw_2_3_4(list_a):
    """the function that appends word to the end of the list."""
    list_a.append('new word')
    return len(list_a), list_a[-1]


def hw_2_3_5(list_a):
    """the function that appends word to the middle of the list."""
    new_index = int(len(list_a) / 2)
    list_a.insert(new_index, 'new middle word')
    return (len(list_a), list_a[new_index])


def hw_2_3_6(list_a):
    """the function that appends word to the middle of the list."""
    del list_a[0]
    return (len(list_a), list_a[0])


def hw_2_3_7(list_a):
    """the function that removes the word 'word' from the list."""
    # list_a.remove('word')
    text = ' '.join(list_a)
    text = text.replace('word', '')
    list_a = text.split()
    return list_a


if __name__ == '__main__':
    assert hw_2_3_1(['zero', 'one', 2, 'apple', 1, 2]) == 'apple'
    assert hw_2_3_1([999, 22, [1, 2, 2, 2], 2, 'apple', [33, 22, 33], 1, 2]) == [33, 22, 33]
    print('hw_2_3_1 done')
    assert hw_2_3_2(['first', 'second']) == 's'
    assert hw_2_3_2(['notebook', 'pan', 'football']) == 'p'
    print('hw_2_3_2 done')
    assert hw_2_3_3(['first', 'second']) == 'd'
    assert hw_2_3_3(['notebook', 'pan', 'football']) == 'l'
    print('hw_2_3_3 done')
    assert hw_2_3_4(['first', 'second']) == (3, 'new word')
    assert hw_2_3_4(['notebook', 'pan', 'football']) == (4, 'new word')
    print('hw_2_3_4 done')
    assert hw_2_3_5(['first', 'second']) == (3, 'new middle word')
    assert hw_2_3_5(['notebook', 'pan', 'football']) == (4, 'new middle word')
    print('hw_2_3_5 done')
    assert hw_2_3_6(['first', 'second']) == (1, 'second')
    assert hw_2_3_6(['notebook', 'pan', 'football']) == (2, 'pan')
    print('hw_2_3_6 done')
    assert hw_2_3_7(['one', 'word', 'one']) == ['one', 'one']
    assert hw_2_3_7(['word', 'word', 'word']) == []
    assert hw_2_3_7(['world', 'wood', 'word']) == ['world', 'wood']
    assert hw_2_3_7(['one']) == ['one']
    assert hw_2_3_7([]) == []
    print('hw_2_3_7 done')
    print('happy end)')