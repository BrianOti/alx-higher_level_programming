#!/usr/bin/python3
import hidden_4


def main():
    lenth = dir(hidden_4)
    for i in range(len(lenth)):
        if(lenth[i][0] != '_'):
            print("{}".format(lenth[i]))


if __name__ == "__main__":
    main()
