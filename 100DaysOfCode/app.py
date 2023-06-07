str_1 = "adfghjklmbcezxvnsopyq"
str_2 = ""

def printer_error(s):
    errors = []
    length = len(s)

    for x in s:
        if ord("a") <= ord(x) <= ord("m"):
            continue
        errors.append(x)
    return f"{len(errors)}/{length}"

def is_triangle(a, b, c):
    if (a == 0 or a is None) or (b == 0 or b is None) or (c == 0 or c is None):
        return 0
    else:
        if (a + b > c) and (b + c > a) and (c + a > b):
            return True
        else:
            return False
