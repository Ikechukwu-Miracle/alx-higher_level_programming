#!/ysr/bin/python3

def magic_calculation(a, b):
    re = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            re += (a ** b) / i
        except:
            re = b + a
            break

    return re
