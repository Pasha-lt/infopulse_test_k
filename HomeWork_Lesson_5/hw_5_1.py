def foo(*args):
    list_a = list(set(args))
    list_a.sort()
    return list_a[1]


print(foo(5, 6, 6, 7, 8, 8, 4, 4, 4, 3, 3))
