#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    digit = number % 10
elif number == 0:
    digit = 0
else:
    digit = (number * (-1))
    digit = digit % 10
if digit > 5:
    conclusion = "grater than 5"
elif digit == 0:
    conclusion = "0"
elif digit < 6:
    conclusion = "less than 6 and not 0"
print(f"Last digit of {number} is {digit} and is {conclusion}")
