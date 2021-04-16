def is_year_leap(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


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
