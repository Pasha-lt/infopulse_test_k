def is_year_leap(year):
    return bool(year % 4 == 0)


def triangle(side_a, side_b, side_c):
    return (side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a)


def hw_4_2_3(side_a, side_b, side_c):
    if not (side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a):
        return 'Not a tringle'
    if (side_a == side_b and side_b != side_c) or (side_c == side_b and side_b != side_a) or (
            side_a == side_c and side_c != side_b):
        return 'Isosceles triangle'
    if side_a == side_b and side_b == side_c:
        return 'Equilateral triangle'
    else:
        return 'Versatile triangle'


def distance(x1, y1, x2, y2):
    return f'Растояние между x2 и x1: {abs(x2 - x1)}. Растояние между y2 и y1: {abs(y2 - y1)}'


if __name__ == '__main__':
    x1 = round(float(input('Введите x1 параметр: ')), 2)
    y1 = round(float(input('Введите y1 параметр: ')), 2)
    x2 = round(float(input('Введите x2 параметр: ')), 2)
    y2 = round(float(input('Введите y2 параметр: ')), 2)
    print(distance(x1, y1, x2, y2))
