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
print(f"number:{number} digit:{digit}")
