#!/usr/bin/env python
from math import factorial

def int_to_digits(x):
    str_x = str(x)
    return [int(d) for d in str_x]

def is_curious(x):
    digits = int_to_digits(x)
    x_facts = [factorial(x) for x in digits]
    return sum(x_facts) == x

if __name__ == "__main__":
    curious_nums = [x for x in range(3, 2 * (10 ** 6)) if is_curious(x)]
    print(sum(curious_nums))
