def hw_3_3_1():
    n=0
    while n <10:
        print(n)
        n+=1


def hw_3_3_2():
    n=20
    while n:
        print(n, end=' ')
        n-=1


def hw_3_3_3(number_a):
    counter = -1
    while True:
        counter +=1
        if not number_a%2:
            number_a /=2
        else:
            print(number_a)
            print(counter)
            return number_a, counter


