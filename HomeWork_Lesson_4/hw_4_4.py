def song_la_la_la(how_strings, la_in_string, number=0):
    print(number, type(number))
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

    return (song)


if __name__ == '__main__':
    print(song_la_la_la(3, 4, 1))
