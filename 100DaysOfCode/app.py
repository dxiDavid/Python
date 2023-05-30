myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_array = [2, 2]

def loop_and_square(array):

    squared_list = [x**2 for x in array]
    print(sum(squared_list))


loop_and_square(new_array)
