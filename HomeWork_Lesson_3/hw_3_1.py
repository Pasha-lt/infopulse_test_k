def hw_3_1_1(string_a):
    print(string_a[2])
    return string_a[2]

def hw_3_1_2(string_a):
    print(string_a.split()[1][-2])
    return string_a.split()[1][-2]

def hw_3_1_3(string_a):
    print(string_a.split()[2][:5])
    return string_a.split()[2][:5]

def hw_3_1_4(string_a):
    print(string_a[:-2])
    return string_a[:-2]

def hw_3_1_5(string_a):
    print(string_a[::2])
    return string_a[::2]

def hw_3_1_6(string_a):
    print(string_a[1::2])
    return string_a[1::2]

def hw_3_1_7(string_a):
    print(string_a[::-1])
    return string_a[::-1]

def hw_3_1_8(string_a):
    print(string_a[-1:0:-2])
    return string_a[-1:0:-2]

def hw_3_1_9(string_a):
    print(string_a[-2:0:-2])
    return string_a[-2:0:-2]

def hw_3_1_10(string_a):
    print(string_a[-2:1:-1])
    return string_a[-2:1:-1]

def hw_3_1_11(string_a):
    print(len(string_a))
    return len(string_a)

if __name__ == '__main__':
    assert hw_3_1_1('stone') == 'o'
    print('hw_3_1_1 - ok')
    assert hw_3_1_2('the stone is cold') == 'n'
    print('hw_3_1_2 - ok')
    assert hw_3_1_3('stone is coldest then fire') == 'colde'
    print('hw_3_1_3 - ok')
    assert hw_3_1_4('stone is coldest then fire') == 'stone is coldest then fi'
    print('hw_3_1_4 - ok')
    assert hw_3_1_5('stone is coldest then fire')=='soei ods hnfr'
    print('hw_3_1_5 - ok')
    assert hw_3_1_6('stone is coldest then fire')=='tn sclette ie'
    print('hw_3_1_6 - ok')
    assert hw_3_1_7('stone is coldest then fire')=='erif neht tsedloc si enots'
    print('hw_3_1_7 - ok')
    assert hw_3_1_8('stone is coldest then fire')=='ei ettelcs nt'
    print('hw_3_1_8 - ok')
    assert hw_3_1_9('stone is coldest then fire')=='rfnh sdo ieo'
    print('hw_3_1_9 - ok')
    assert hw_3_1_10('stone is coldest then fire')=='rif neht tsedloc si eno'
    print('hw_3_1_10 - ok')
    assert hw_3_1_11('stone is coldest then fire')==26
    print('hw_3_1_11 - ok')
    print('good job')

