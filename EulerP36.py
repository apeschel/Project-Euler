#!/usr/bin/env python

def is_palindrome(s):
    return s == s[::-1]

def is_palindromic(x):
    bin_x = bin(x)[2:]
    str_x = str(x)
    return (is_palindrome(str_x) and is_palindrome(bin_x))

if __name__ == "__main__":
    palindomes = [x for x in range(10 ** 6) if is_palindromic(x)]
    print(sum(palindomes))
