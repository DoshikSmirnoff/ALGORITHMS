"""
Вам дано четырехзначное число без ведущих нулей.
Вам нужно переставить в нем цифры таким образом, чтобы получившееся число было минимально возможным
и не содержало ведущих нулей.

Входные данные
В первой строке записано единственное четырехзначное число х (1000 ≤ x ≤ 9999).

Выходные данные
Выведите единственное число — минимальное число без ведущих нулей, полученное перестановкой цифр из исходного числа.
"""

def four_digit_number(num: int) -> int:

    sorted_num_list = sorted(list(str(num)))

    if sorted_num_list.count("0") > 1:
        for num in sorted_num_list:
            if num != "0":
                main_num = num
                sorted_num_list.pop(sorted_num_list.index(main_num))
                sorted_num_list.insert(0, main_num)
                break
        print(int("".join(sorted_num_list)))
    elif sorted_num_list.count("0") == 1:
        sorted_num_list.pop(0)
        sorted_num_list.insert(1, "0")
        print(int("".join(sorted_num_list)))
    else:
        print(int("".join(sorted_num_list)))

four_digit_number(1020)