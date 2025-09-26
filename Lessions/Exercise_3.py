from array import array

"""
Дан целочисленный массив размера N. Найти максимальное количество его
одинаковых элементов.
"""

def max_count(arr: list):
    # [1, 2, 2, 2, 5, 4, 0, 0, 0, 0] -> 4
    new_set = set(arr)
    new_dict = dict.fromkeys(new_set, 0)

    for num in arr:
        if num in new_dict:
            new_dict[num] += 1

    print(max(new_dict.values()))

N = int(input("Введите размер массива: "))
arr = array('i', [int(input(f"arr[{i}] = ")) for i in range(N)])

max_count(arr)
