# -----------------------------------------------------------------------------
# Created by Ulysses Carlos on 07/18/2020 at 10:00pm
#
# Lexicon.py
#
# -----------------------------------------------------------------------------


def ascii_atoi(string):
    """
    Covert a string into a number, assuming that the string uses ascii numbers.
    """
    # First, first digit. If sign is - or +, set sign

    if len(string) < 1:
        raise Exception("Cannot convert an empty string.")

    sign = 1
    if (string[0] == '+'):
        string = string[1:]
    elif (string[0] == '-'):
        string = string[1:]
        sign = -1

    # Now check if the rest of the string is valid.
    if not string:
        raise Exception("String must contain characters past "
                        + "the sign character.")

    if not string.isdigit():
        raise ValueError("String contains non-alphanumerical characters.")

    value = 0
    length = len(string)
    for i in range(0, length):
        value *= 10
        value += (ord(string[i]) - ord('0'))

    return sign * value


def scan(string):
    """
    Split a user-specified string and convert it to tuples used for the game.
    """
    # Convert the string to lowercase:
    string = string.lower()

    tuple_list = []

    direction_list = ['north', 'south', 'east', 'west',
                      'up', 'down', 'left', 'right',
                      'back']

    verb_list = ['go', 'run', 'stop', 'kill', 'eat']
    stop_list = ['the', 'in', 'of', 'from', 'at', 'it']
    noun_list = ['door', 'bear', 'princess', 'cabinet']

    words = string.split()

    for w in words:
        # Check if w is in direction list
        found_word = False
        if not w.isalnum:
            tuple_list.append(("error", w))
            continue

        if w.isdigit():
            tuple_list.append(("number", int(w)))
            # tuple_list.append(("number", ascii_atoi(w)))
            continue

        for i in direction_list:
            if w == i:
                tuple_list.append(("direction", w))
                found_word = True
                break

        for i in verb_list:
            if w == i:
                tuple_list.append(("verb", w))
                found_word = True
                break

        for i in stop_list:
            if w == i:
                tuple_list.append(("stop", w))
                found_word = True
                break
        for i in noun_list:
            if w == i:
                tuple_list.append(("noun", w))
                found_word = True
                break

        if not found_word:
            tuple_list.append(('error', w.upper()))

    return tuple_list
