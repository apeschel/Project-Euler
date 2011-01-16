#!/usr/bin/python

dic = {1:1}

def chain_len(n):
    if n in dic:
        return dic[n]
    elif n % 2 == 0:
        dic[n] = 1 + chain_len(n // 2)
        return dic[n]
    else:
        dic[n] = 1 + chain_len((3 * n) + 1)
        return dic[n]

if __name__ == '__main__':
    max_len = 0
    max_n = 0
    for n in range(1,1000000):
        length = chain_len(n)
        if length > max_len:
            max_len = length
            max_n = n
    print(max_n)
