"""
Завдання 1
Реалізувати дві функції для видачі решти:
1. Жадібний алгоритм (find_coins_greedy)
2. Динамічне програмування (find_min_coins)
Порівняти ефективність обох підходів.
"""

import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result


def main():
    print("Сума 113:")
    print(f"  Жадібний:    {find_coins_greedy(113)}")
    print(f"  Дин. прогр.: {find_min_coins(113)}")

    print("\nПорівняння часу для різних сум:")
    print(f"{'Сума':>8} | {'Жадібний':>12} | {'DP':>12}")
    print("-" * 42)

    for amount in [113, 1000, 10000, 100000]:
        t_greedy = timeit.timeit(lambda: find_coins_greedy(amount), number=100)
        t_dp = timeit.timeit(lambda: find_min_coins(amount), number=3) / 3 * 100
        print(f"{amount:>8} | {t_greedy:>12.6f} | {t_dp:>12.6f}")

    print("\nДетальні висновки наведено у файлі readme-hw-10-1.md")


if __name__ == "__main__":
    main()
