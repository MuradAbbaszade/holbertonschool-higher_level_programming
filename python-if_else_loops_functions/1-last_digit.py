#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    print("{} and is greater than 5".format(str))
elif last_digit == 0:
    print("{} and is 0".format(str))
else:
    print("{} and is less than 6 and not 0".format(str))
