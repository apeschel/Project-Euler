#!/usr/bin/env
from math import floor

def num_to_digits(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x = floor(x / 10)

    return digits


def digit_sum(x):
    digits = num_to_digits(x)
    total = 0
    for digit in digits:
        total = total + (digit ** 5)

    return total


if __name__ == "__main__":
    MIN = 2
    MAX = 354294
    result = 0
    for x in range(MIN, MAX):
        total = digit_sum(x)
        if total == x:
            result = result + x

    print(result)
