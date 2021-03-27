def hw_2_1_1(string_a):
    """the function checks if the value consists of numbers"""
    return str(string_a).isdigit()


def hw_2_1_2(string_a):
    """the function counts spaces"""
    return (string_a.count(' '))


def hw_2_1_3(string_a):
    """the function counts spaces"""
    return (string_a.count('.'))


def hw_2_1_4(string_a):
    """this function makes an inscription in the middle"""
    string_a = string_a.center(100, ' ')
    return (len(string_a))


def hw_2_1_5(string_a):
    """function makes the first letters of words large"""
    return string_a.title()


def hw_2_1_6(string_a):
    """the function checks the end of the sentence. must ing"""
    string_a = string_a.lower()
    string_a = string_a.replace(' ', '').replace('.', '').replace('!', '').replace('?', '')
    return (string_a[-3:])


def hw_2_1_7(string_a):
    """the function looks for the index of the first letter 'a'"""
    return string_a.find('a')


def hw_2_1_8(string_a):
    """the function splits the string by space into elements"""
    return string_a.split()


def hw_2_1_9(string_a):
    """the function removes leading and trailing spaces"""
    string_a = string_a.lstrip().rstrip()
    return string_a

if __name__ == '__main__':
    assert hw_2_1_1(123) == True
    assert hw_2_1_1('wq12') == False
    print('hw_2_1_1 done')
    assert hw_2_1_2('') == 0
    assert hw_2_1_2('zero') == 0
    assert hw_2_1_2('one space') == 1
    assert hw_2_1_2('we have three spases') == 3
    assert hw_2_1_2('  we have six  spases') == 6
    print('hw_2_1_2 done')
    assert hw_2_1_3('') == 0
    assert hw_2_1_3('zero dot') == 0
    assert hw_2_1_3('one dot.') == 1
    assert hw_2_1_3('.we. have three   . dots') == 3
    assert hw_2_1_3('we have six dots......') == 6
    print('hw_2_1_3 done')
    assert hw_2_1_4('Homework') == 100
    print('hw_2_1_4 done')
    assert hw_2_1_5('two words') == 'Two Words'
    assert hw_2_1_5('I am going to travel round the world') == 'I Am Going To Travel Round The World'
    assert hw_2_1_5('') == ''
    assert hw_2_1_5('i') == 'I'
    print('hw_2_1_5 done')
    assert hw_2_1_6('My hobby is reading') == 'ing'
    assert hw_2_1_6('My hobby is readnig') != 'ing'
    assert hw_2_1_6('Do you mind me being here while you’re working???') == 'ing'
    assert hw_2_1_6('ing') == 'ing'
    assert hw_2_1_6('') != 'ing'
    print('hw_2_1_6 done')
    assert hw_2_1_7('jkladsa') == 3
    assert hw_2_1_7('sfsd') == -1
    assert hw_2_1_7('asfsd') == 0
    print('hw_2_1_7 done')
    assert hw_2_1_8('dsd fdfs fdsf') == ['dsd', 'fdfs', 'fdsf']
    assert hw_2_1_8('   ') == []
    assert hw_2_1_8('  2 ') == ['2']
    print('hw_2_1_8 done')
    assert hw_2_1_9('    ffdsfdsf           f sdfdsf    ') == 'ffdsfdsf           f sdfdsf'
    assert hw_2_1_9('the moon ! ') == 'the moon !'
    print('hw_2_1_9 done')
    print('happy end)')