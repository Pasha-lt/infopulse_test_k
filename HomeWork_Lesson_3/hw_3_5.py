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


