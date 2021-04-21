# pip install pyexcel

# Задание 5
# Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (в первой строке заголовки колонок)
#     • Посчитайте сколько отделов на фирме +
#     • Определите максимальную зарплату
#     • Определите максимальную зарплату в каждом отделе
#     • Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в новый файл
# Подсказка: используйте словари!!!

import pyexcel

my_array = pyexcel.get_array(file_name="sheet_department.ods")
my_array = my_array[1:]

# Создаем список
my_dict = {}
for department in my_array:
    my_dict[f'{department[0]} {department[1]}'] = department[2:]


# Определяем количество отделов.
list_department = []
for department in my_dict.values():
    list_department.append(department[0])

print(f'Количество отделов - {len(set(list_department))}')

# Ищем максимальную зарплату.
list_key = list(my_dict.keys())

finish_salary = 0
for salary in list_key:
    if my_dict[f'{salary}'][1] > finish_salary:
        finish_salary = my_dict[f'{salary}'][1]
print(f'Максимальная зарплата {finish_salary}')

# Максимальная зарплата в отделе
dict_department = {}
for point in list_key:
    department = my_dict[f'{point}'][0]
    if department in dict_department.keys():
        if my_dict[f'{point}'][1] > dict_department[f'{department}'][0]:
            dict_department[f'{my_dict[f"{point}"][0]}'] = my_dict[f'{point}'][1], point
        else:
            pass
    else:
        dict_department[f'{my_dict[f"{point}"][0]}'] = my_dict[f"{point}"][1], point

print(dict_department)

# Запись результата в файл
data_fof_new = ''
for key, value in dict_department.items():
    data_fof_new += f'{key} - {value} \n'

with open('new_sheet_6_5', 'w') as file:
    file.write(data_fof_new)
