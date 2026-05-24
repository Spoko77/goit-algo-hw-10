"""
Завдання 2
Обчислити інтеграл f(x) = x^2 на [0, 2] методом Монте-Карло.
Порівняти з аналітичним розв'язком та з функцією scipy.integrate.quad.
"""

import random
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo(func, a, b, n=100000):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += func(x)
    return (b - a) * total / n


def main():
    a, b = 0, 2

    # Аналітично: інтеграл x^2 від 0 до 2 = 8/3
    analytical = (b**3 - a**3) / 3

    quad_result, quad_error = spi.quad(f, a, b)

    print(f"Інтеграл f(x) = x^2 на [{a}, {b}]:\n")
    print(f"Аналітично: {analytical:.6f}")
    print(f"scipy.quad: {quad_result:.6f}  (похибка: {quad_error:.2e})")
    print()
    print("Метод Монте-Карло:")
    for n in [1000, 10000, 100000, 1000000]:
        mc = monte_carlo(f, a, b, n)
        diff = abs(mc - analytical)
        print(f"  N = {n:>7}: {mc:.6f}  (різниця: {diff:.6f})")

    print("\nДетальні висновки наведено у файлі readme-hw-10-2.md")


if __name__ == "__main__":
    main()
