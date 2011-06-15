#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def coin_combinations(goal, coin_list):
    if len(coin_list) == 0:
        return 0

    total = coin_combinations(goal, coin_list[1:]))
    max_coin_value = coin_list[0]

    if max_coin_value > goal:
        return total + 0
    elif max_coin_value == goal:
        return total + 1
    else:
        return total + coin_combinations(goal - max_coin_value, coin_list)


def main():
    goal = 200
    coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
    combinations = coin_combinations(goal, coin_values)
    print combinations


if __name__ == "__main__":
    main()
