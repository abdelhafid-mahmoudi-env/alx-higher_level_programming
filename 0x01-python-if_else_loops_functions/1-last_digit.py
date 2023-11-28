#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
number = random.randint(-10000, 10000)

# Messages for different conditions
str_greater_than_5 = " and is greater than 5"
str_zero = " and is 0"
str_less_than_6_not_0 = " and is less than 6 and not 0"

# Determine the last digit
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Print the appropriate message based on the last digit
if last_digit > 5:
    message = str_greater_than_5
elif last_digit == 0:
    message = str_zero
else:
    message = str_less_than_6_not_0

# Output the result
print(f"Last digit of {number} is {last_digit}{message}")
