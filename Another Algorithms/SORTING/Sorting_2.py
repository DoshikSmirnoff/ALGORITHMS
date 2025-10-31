"""
СОРТИРОВКА ВЫБОРОМ

Требуется отсортировать массив по неубыванию (по возрастанию) методом "выбор максимума".

Входные данные
В первой строке вводится одно натуральное число, не превосходящее 1000 – размер массива.
Во второй строке задаются N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).

Выходные данные
Вывести получившийся массив.
"""

num = int(input())
num_list = [int(input()) for i in range(num)] # 4 2 6

def sorted_2(list_numbers):

    for i in range(len(list_numbers)):
        current_min_num = list_numbers[i]
        num_index = i

        for j in range(i + 1, len(list_numbers)):
            if list_numbers[j] < current_min_num:
                current_min_num = list_numbers[j]
                num_index = j

        list_numbers[i], list_numbers[num_index] = list_numbers[num_index], list_numbers[i]

    return list_numbers

print(sorted_2(num_list))
