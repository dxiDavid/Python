listOne = [34, 15, 88, 2]
listTwo = [34, -345, -1, 100]

def find_smallest_int(listOfIntegers):
    listOfIntegers.sort()
    print(listOfIntegers)
    return listOfIntegers[0]

find_smallest_int(listTwo)
