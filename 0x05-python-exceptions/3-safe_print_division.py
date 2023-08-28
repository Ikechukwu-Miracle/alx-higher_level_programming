#!/usr/bin/python3

def safe_print_division(a, b):
    resDiv = 0

    try:
        resDiv = a / b
    except (TypeError, ZeroDivisionError):
        resDiv = None
    finally:
        print("Inside result: {}".format(resDiv))

    return resDiv
