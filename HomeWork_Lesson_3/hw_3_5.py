text = \
    """
    We are not  what we should be!
    We are not what we need to be.
    But at least we are not what we used to be
    (Football Coach)
    """


def hw_3_5_1(text_string):
    return len(text_string.split())


def hw_3_5_2(text_string):
    new_string = ''
    for symbol in text_string:
        new_string += symbol.strip('!').strip('.')
    return new_string


def hw_3_5_3(text):
    text = text.replace('.', '').replace(')', '').replace('(', '').replace('!', '').replace('\n', '').replace('  ', '')
    text_string = text.lower().split()
    return sorted(text_string)


def hw_3_5_4(text):
    text = text.replace('.', '').replace(')', '').replace('(', '').replace('!', '').replace('\n', '').replace('  ', '')
    text_string = text.lower().split()
    dict_counter = {}
    for word in text_string:
        if word in dict_counter:
            dict_counter[word] += 1
        else:
            dict_counter[word] = 1
    return (dict_counter)
