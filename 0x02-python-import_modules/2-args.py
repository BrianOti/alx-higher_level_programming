#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    arg_len = len(sys.argv) - 1
    if arg_len == 1:
        print("{:d} argument:".format(arg_len))
    elif arg_len == 0:
        print("{:d} arguments.".format(arg_len))
    else:
        print("{:d} arguments:".format(arg_len))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1

if __name__ == "__main__":
    main()
