def convert_to_number(string):
    converted_number = None

    if "." in string:
        converted_number = float(string)
        print(converted_number)
    else:
        converted_number = int(string)
        print(converted_number)

    return converted_number

def negate(number):

    number_to_convert = number

    if number_to_convert < 0:
        print(number_to_convert, "is already negative")
    else:
       number_to_convert = number - number*2

    return number_to_convert

def greet(user_name):
    user_name = input("what is your name")
    return f"Hello, {user_name} how are you doing today?"

