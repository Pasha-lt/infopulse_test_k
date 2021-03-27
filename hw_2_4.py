def h_w_2_4_1():
    dict_a = {'title': 'apple', 'price': 20, 'ingredients': ['red', 'green']}
    dict_a['description'] = 'some text'
    dict_a['price'] += 100
    dict_a['ingredients'].append('yellow')
    print(len(dict_a['ingredients']))
    del dict_a['description']
    return dict_a


if __name__ == '__main__':
    assert h_w_2_4_1() == {'title': 'apple', 'price': 120, 'ingredients': ['red', 'green', 'yellow']}
    print('happy end)')
