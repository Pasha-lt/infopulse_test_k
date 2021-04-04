def hw_3_4_1(list_a):
    while list_a:
        print(list_a[0])
        list_a.pop(0)


def hw_3_4_2(string_a):
    while string_a:
        print(string_a[0])
        string_a = string_a[1:]
        print(string_a)


def hw_3_4_3(list_a):
    list_a.sort()
    while list_a:
        print(list_a[0])
        list_a.pop(0)


def hw_3_4_3(list_a):
    list_a.sort()
    while list_a:
        print(list_a[0])
        list_a.pop(0)


def hw_3_4_4(list_a):
    predecessor = ''
    counter = 1
    max_number = 0
    for number in list_a:
        if number == predecessor:
            counter += 1
            if counter > max_number:
                max_number = counter
                print(max_number)
        else:
            counter = 1
        predecessor = number
    return max_number
