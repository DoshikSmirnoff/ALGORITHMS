"""
Алгоритм вычисления Функций F(n) и G(n), где n - целое число, задан
следующими соотношеннями.
F(n)= 2×(G(n-3) + 8);
G(n) = 2 х n, если n < 10;
G(n) = G(n-2) + 1, ecли n ≥ 10.
Чему равно значение выражения F(15 548)?
"""

import sys

sys.setrecursionlimit(16000)

def func_g(n: int) -> int:
    if n < 10:
        return 2 * n
    else:
        return func_g(n - 2) + 1

print(func_g(15548))

def func_f(n: int) -> int:
    return 2 * (func_g(n - 3) + 8)

print(func_f(15548))