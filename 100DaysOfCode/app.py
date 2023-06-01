
"""

def simple_multiplication(number):
    number_var = None

    if number % 2 == 0:
        number_var = number * 8
    else:
        number_var = number * 9

    return number_var

"""

def reverse_seq(n):
    if n is None or n <= 0:
        return 0
    else:
        numbers_list = [n]

        while numbers_list[-1] != 1:
            number = numbers_list[-1] - 1
            numbers_list.append(number)

        #return numbers_list
        print(numbers_list)


reverse_seq(8)
