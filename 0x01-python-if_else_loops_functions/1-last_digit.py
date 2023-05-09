#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# get the last digit
last_digit = abs(number) % 10
# Check if the last digit of number is greater than 5
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
# Check if the last digit is zero
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
# Check if last digit is less than 6 and not 0
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit}"
          "and is less than 6 and not 0")
