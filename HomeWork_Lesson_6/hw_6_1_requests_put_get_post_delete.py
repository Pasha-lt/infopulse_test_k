# Задание 1 (Обязательное всем, кроме части со звёздочкой!!!!)
# Тестовое приложение с REST API: http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
#     • Создаём книгу POST /books/, вы запоминаете его id.
#     • Проверяете, что она создалась и доступна по ссылке GET/books/[id]
#     • Проверяете, что она есть в списке книг по запросу GET /books/
#     • Изменяете данные этой книги методом PUT /books/[id]/
#     • Проверяете, что она изменилась и доступна по ссылке /books/[id]
#     • Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
#     • Удаляете эту книгу методом DELETE /books/[id].
# Все проверки делать программно, а не глазами, т.е. проверить,
# что в теле response данные такие же как в вашем исходном словаре путём сравнения значений в словарях
#
# Второй скрипт:
# тоже самое с ролями. Здесь немного поинтересней, т.к. есть связка с книгой, которая уже должна существовать.
# Создайте книгу заранее в этом же скрипте, не надейтесь на книги, которые вы видите, их кто-то другой может удалить.
#
# Третий скрипт:
# Поэкспериментируйте создавать книги и роли с неправильными данными. Посмотрите тело и статус код ответов.
# Попробуйте создать роль с ссылкой на книгу, которой нет. Посмотрите тело и статус код response.
# ** Попробуйте воспользоваться http.client вместо requests. Ощутите разницу 😊

import requests

# Открываем файл
# t = requests.get('http://pulse-rest-testing.herokuapp.com/books')
# print(t.json()[0]) # Берем одну книгу чтобы посмотреть какие ключи мы можем использовать.
# print(t.url)  # Если мы передали какие-то значения то выводим
# print(t.text)  # ответ сервера
# print(t.status_code)  # статус код
# print(t.headers)  # заголовки ответов
########################################

# #Script 1
# # Отправляем книгу
# payload = {'title': 'Son of the Wolf', 'author': 'Jack London'}
# r = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=payload)
# print(r.text)  # выводит что мы сосзади таким образом мы можем увидеть айди
# print(r.json()['id'])
# id_my_book = r.json()['id']
#
# # Получаем нужноую нам книгу.
# t = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
# assert t.json()['id'] == id_my_book and t.json()['title'] == 'Son of the Wolf' and t.json()['author']=='Jack London'
# print('Книга создалась успешно')
#
# # меняем книгу
# payload = {'title': "The Lancer's Wife", 'author': "Guy de Maupassant"}
# q = requests.put(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}', data=payload)
# print(q.text)  # Выводим результат нашего изминения
#
# # проверяем изминения
# t = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
# assert t.json()['id'] == id_my_book and t.json()['title'] == "The Lancer's Wife" and t.json()['author']=="Guy de Maupassant"
# print('Книга изменилась успешно')
# print(t.json())
#
# # Удаление обьекта
# d = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
# assert d.status_code == 204
# print('Книга удалилась успешно')
#
# ################################
# Script 2
# Создаем книгу
payload = {'title': 'Son of the Wolf', 'author': 'Jack London'}
r = requests.post('http://pulse-rest-testing.herokuapp.com/books', data=payload)
print(r.text)  # выводит что мы сосзади таким образом мы можем увидеть айди
print(r.json()['id'])
id_my_book = r.json()['id']

# Проверяем книгу
t = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert t.json()['id'] == id_my_book and t.json()['title'] == 'Son of the Wolf' and t.json()['author'] == 'Jack London'
print('Книга создалась успешно')

# Создаем Персонажа
payload = {'name': 'young wolf', 'type': 'Wolf', 'level': 5, 'book': f'{id_my_book}'}
r = requests.post('http://pulse-rest-testing.herokuapp.com/roles', data=payload)
id_person = r.json()['id']

# Проверяем нужного нам персонажа.
t = requests.get(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}')
assert t.json()['id'] == id_person and t.json()['name'] == 'young wolf' and t.json()['type'] == 'Wolf' and t.json()[
    'level'] == 5
print('Персонаж создался успешно')

# меняем левел и тип персонажа
payload = {'name': 'young wolf', 'type': 'Wolf+', 'level': 10, 'book': f'{id_my_book}'}
r = requests.put(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}', data=payload)

# проверяем изминения персонажа
assert r.json()['id'] == id_person and r.json()['name'] == 'young wolf' and r.json()['type'] == 'Wolf+' and r.json()[
    'level'] == 10
print('Персонаж изменилась успешно')
print(r.json())

# Удаление книги
d = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{id_my_book}')
assert d.status_code == 204
print('Книга удалилась успешно')

# Удаление Персонажа
d = requests.delete(f'http://pulse-rest-testing.herokuapp.com/roles/{id_person}')
assert d.status_code == 204
print('Персонаж удалилась успешно')
################################
# # удаление циклом по айди
# for number in range(1541, 1555):
#     t = requests.get(f'http://pulse-rest-testing.herokuapp.com/books/{number}')
#     if t.status_code == 404:
#         print(f'c таким айди нет {number}')
#     else:
#         print(f'Удаляем {t.json()}')
#         d = requests.delete(f'http://pulse-rest-testing.herokuapp.com/books/{number}')

# передаем пользовательский агент
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)

# pprint.pprint(t.json())
