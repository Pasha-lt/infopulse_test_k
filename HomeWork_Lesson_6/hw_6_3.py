# Задание 3
# Записывает в новый файл все слова в алфавитном порядке из другого файла с текстом. Каждое слово на новой строке.
# Рядом со словом укажите сколько раз оно встречалось в тексте

dict_with_word = {}

with open('exaple_for_6_3.txt', 'r') as file:
    text = file.read()
    text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('"', '')
    text = text.title()

    for word in text.split():
        if not dict_with_word.get(word):
            dict_with_word[word] = 1
        else:
            dict_with_word[word] += 1

list_key = list(dict_with_word.keys())
list_key.sort()

for word in list_key:
    with open('done_file_6_3', 'a') as file:
        file.write(f'{word} - {dict_with_word[word]}\n')
