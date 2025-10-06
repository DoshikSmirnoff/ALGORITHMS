


def main():
    n, k = map(int, input().split())

    if n % 10 == 0 or n == 0 or k == 0:
        print(n)

    elif n % 10 == 5:
        n += 5
        print(n)

    else:
        if n % 2 != 0:
            n += n % 10
            k -= 1

        full_iter = k // 4
        remainder = k % 4

        for i in range(remainder):
            n += n % 10

        n += full_iter * 20

        print(n)


if __name__ == "__main__":
    main()