
"""
[3, 5, 1, 8, 10] -> по возр




"""

def sort_3(num_list):

    for i in range(1, len(num_list)):
        first_num = num_list[i]
        num_index = i - 1

        while first_num < num_list[num_index] and num_index >= 0:
            num_list[num_index + 1], num_list[num_index] = num_list[num_index], num_list[num_index + 1]
            num_index -= 1

    return num_list

print(sort_3([3, 5, 1, 8, 10]))

# написать в обратную сторону
# разобраться почему сложность разная
# + merge sort