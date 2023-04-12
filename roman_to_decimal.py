import unittest

def roman_to_decimal(roman):
    total = 0
    for letter in roman:
        if letter == 'I':
            total += 1
        elif letter == 'V':
            if total > 0:
                total = -1
            total += 5
        elif letter == 'X':
            if total > 0:
                total = -1
            total += 10
    return total

