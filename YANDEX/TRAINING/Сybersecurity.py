def main():
    s = input().strip()
    n = len(s)

    new_dict = {}
    for char in s:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1

    repeated_pairs = 0
    for i in new_dict.values():
        if i > 1:
            repeated_pairs += i * (i - 1) // 2

    result = (n * (n - 1) // 2) - repeated_pairs + 1
    print(result)

if __name__ == '__main__':
    main()