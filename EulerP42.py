#!/usr/bin/env python
import sys

def char_to_position(ch):
    ch = ch.lower()
    return (ord(ch) - ord('a') + 1)

def str_to_positions(s):
    return [char_to_position(ch) for ch in s]

def is_triangle_num(x):
    for n in range(1000):
        if (n ** 2) + n - (2 * x) == 0:
            return True

    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    input_file = sys.argv[1]
    words = []
    total = 0

    for line in open(input_file):
        line = line.strip()
        line = line.split(',')
        words = words + line

    for (i, word) in enumerate(words):
        words[i] = word.strip('"')

    for word in words:
        value = sum(str_to_positions(word))
        if is_triangle_num(value):
            total = total + 1

    print(total)
