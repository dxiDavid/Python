myArray = ["Keep", "Remove", "Keep", "Remove", "Keep"]


def remove_every_other(array):

    if array is None or len(array) == 0:
        return 0
    else:
        every_other = array[::2]
        return every_other


def check(seq, elem):
    if seq is None and elem is None:
        return 0
    elif elem in seq:
        return True
    else:
        return False

def zero_fuel(distance_to_pump, mpg, fuel_left):

    distance_limit = fuel_left * mpg

    if distance_limit < distance_to_pump:
        return False
    else:
        return True

def to_jaden_case(string):
    return string.title()




