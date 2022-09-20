#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = str(number)
lindex = strnum[-1]
ldigit = int(lindex)
if (ldigit > 5):
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
elif (ldigit < 6 and ldigit != 0):
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
elif (ldigit == 0):
    print(f"Last digit of {number} is {ldigit} and is 0")
