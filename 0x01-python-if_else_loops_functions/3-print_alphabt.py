#!/usr/bin/python3
for letter_code in range(97, 123):
    if letter_code == 101 or letter_code == 113:
        continue
    else:
        letter = chr(letter_code)
        print(letter, end="")
