"""
Рассмотрим три числа a, b и c. Упорядочим их по возрастанию.
Какое число будет стоять между двумя другими?
"""
def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    nums = sorted(list(map(int, input().split())))
    print(nums[1])


if __name__ == '__main__':
    main()