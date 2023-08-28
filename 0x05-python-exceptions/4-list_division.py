#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            resDiv = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            resDiv = 0
        except ZeroDivisionError:
            print("division by zero")
            resDiv = 0
        except TypeError:
            print("wrong type")
            resDiv = 0

        finally:
            new_list.append(resDiv)

    return new_list
