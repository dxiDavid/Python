def count_bits(n):
    bin_string = bin(n)
    ones = []
    bin_list = [x for x in bin_string]

    for item in bin_list:
        if item == "1":
            ones.append(item)

    return len(ones)

count_bits(5)
