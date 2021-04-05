def hw_4_1_1(variable_a=False, variable_b=False):
    if variable_a == False and variable_b == False:
        variable_a = input('Введите первое значение: ')
        variable_b = input('Введите второе значение: ')

    try:
        variable_a, variable_b = float(variable_a), float(variable_b)
    except:
        print(str(variable_a) + str(variable_b))
        return str(variable_a) + str(variable_b)
    print(variable_a + variable_b)
    return variable_a + variable_b

if __name__ == '__main__':
    print(hw_4_1_1())
