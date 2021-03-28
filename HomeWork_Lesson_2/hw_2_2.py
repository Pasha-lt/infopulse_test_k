import decimal


def hw_2_2_1(side_a, side_b):
    """the function count the hypotenuse of a right triangle"""
    hypotenuse = (side_a ** 2 + side_b ** 2) ** 0.5
    return round(hypotenuse, 2)


def hw_2_2_2(number):
    """the function looks for how many fits in the number of tens"""
    return number // 10


def hw_2_2_3(number):
    """the function looks for the sum of a three-digit number"""
    number = str(number)
    return int(number[0]) + int(number[1]) + int(number[2])


def hw_2_2_4(number):
    """the function put an integer n. And output the next even number after it."""
    return int(number / 2) * 2 + 2


def hw_2_2_5(number):
    """the function outputs the fractional part"""
    number = str(number)
    index_point = number.find('.')
    number = number[index_point + 1:]
    return number


def hw_2_2_6(number):
    """the function outputs the first digit of the fractional part"""
    number = str(number)
    index_point = number.find('.')
    number = number[index_point + 1]
    return number


if __name__ == '__main__':
    assert hw_2_2_1(367, 127) == 388.35
    assert hw_2_2_1(3, 4) == 5
    print('hw_2_2_1 right')
    assert hw_2_2_2(9) == 0
    assert hw_2_2_2(10) == 1
    assert hw_2_2_2(99) == 9
    print('hw_2_2_2 right')
    assert hw_2_2_3(101) == 2
    assert hw_2_2_3(999) == 27
    assert hw_2_2_3(334) == 10
    print('hw_2_2_3 right')
    assert hw_2_2_4(5) == 6
    assert hw_2_2_4(4) == 6
    assert hw_2_2_4(0) == 2
    assert hw_2_2_4(1) == 2
    print('hw_2_2_4 right')
    assert hw_2_2_5(343.43) == "43"
    assert hw_2_2_5(0) == "0"
    assert hw_2_2_5(0.432879472348) == "432879472348"
    print('hw_2_2_5 right')
    assert hw_2_2_6(343.43) == "4"
    assert hw_2_2_5(0) == "0"
    assert hw_2_2_6(0.432879472348) == "4"
    print('hw_2_2_6 right')
    print('happy end)')