def hw_4_3_1():
    while True:
        try:
            number = int(input('Введите число: '))
        except:
            continue
        break
    return number


def hw_4_3_2():
    while True:
        word = input('Введите Слово: ')
        if ' ' in word[1:-1]:
            continue
        return word.replace(' ',  '')

if __name__ == '__main__':
    # print(hw_4_3_1())
    print(hw_4_3_2())