#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    argc = len(argv) - 1

    arg_sum = 0

    for i in range(argc):
        arg_sum += int(argv[i + 1])

    print("{}".format(arg_sum))
