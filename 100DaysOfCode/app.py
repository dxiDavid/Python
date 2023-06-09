import re
def disemvowel(string):

    return "".join([x for x in string if not re.findall('[aeiouAEIOU]', x)])

def high_and_low(numbers):
    num_str_list = numbers.split(" ")
    num_list = [int(x) for x in num_str_list]
    num_list.sort()

    return f"{num_list[-1]} {num_list[0]}"


high_and_low("1 2 6 4 5 3 11 8")
