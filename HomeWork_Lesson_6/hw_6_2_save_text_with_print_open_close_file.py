# Задание 2
# Задания из класса про работу с файлами на слайдах 4, 8, 10, 11:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
# (кто сделал с помощью методов – делают с помощью print, кто сделал с помощью print – делают с помощью методов)
# 2. А теперь воспользуйтесь менеджером контекста для файлов (with … as).
import time


def song_la_la_la(how_strings, la_in_string, number=0):
    song = ''
    # 2
    string = ''
    for count_la in range(la_in_string):
        string += 'la '
    # 1
    for count_str in range(how_strings):
        song += string + '\n'
    # 3
    if number == 0:
        song = song[:-2] + '.'
    if number == 1:
        song = song[:-2] + '!'
    return song


my_song = song_la_la_la(3, 4, 1)
filew = open('123.txt', 'w')
filew.write(my_song)
filew.close()

# Save file with print
filewp = open('R123.txt', 'w')
print(my_song, file=filewp)
filew.close()

# use with
# with open('123.txt', 'w')as file:
#     file.write(song_la_la_la(3, 4, 1))

time.sleep(2)  # use sleep because we must wait when file saves
filer = open('123.txt', 'r')
for line in filer:
    print(line, end='')

# use with
# with open('123.txt', 'r')as f:
#     text = f.read()
#     print(text)
