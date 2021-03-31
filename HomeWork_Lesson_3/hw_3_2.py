
def hw_3_2(string_a):
    center_index = int(len(string_a)/2)
    if len(string_a)%2:
        string_a = string_a[center_index+1:] + string_a[:center_index+1]
        print(string_a)
    else:
        string_a = string_a[center_index:] + string_a[:center_index]
        print('d',string_a)
    return string_a

def sumaa(a, b):
    return a+b