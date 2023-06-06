import math
import re

def is_square(num):

    if num < 0:
        return False
    else:
        square_root = int(math.sqrt(num))

        if square_root ** 2 == num:
            return True
        else:
            return False



is_square(77)

def descending_order(num):
    if num is None or num <= 0:
        return 0
    else:
        digits = list(map(int, str(num)))
        digits.sort()
        digits.reverse()

        string_list = list(map(str, digits))
        joined_string = "".join(string_list)

        return int(joined_string)


my_string = 'double  spaced  words'
def reverse_words(text):

    separator = r"\s+"
    reversed_words = []

    matches = re.findall(separator, text)
    if matches:
        separator = matches[0]

    word_list = re.split(separator, text)

    for word in word_list:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)

    print(separator.join(reversed_words))
    return separator.join(reversed_words)

reverse_words(my_string)
