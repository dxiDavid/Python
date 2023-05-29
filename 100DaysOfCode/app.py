listOne = [34, 15, 88, 2]
listTwo = [34, -345, -1, 100]
listThree = []

def find_smallest_int(listOfIntegers):
    listOfIntegers.sort()

    if len(listOfIntegers) == 0:
        print("List is empty")
    else:
        print(listOfIntegers)


find_smallest_int(listOne)
find_smallest_int(listTwo)
find_smallest_int(listThree)
