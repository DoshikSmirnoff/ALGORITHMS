# list_clear = [0, 1, 2, 3, 4]
#
# third_element = list_clear.pop(2)
# list_clear.insert(2, 10)
# # list_clear.clear()
# print(list_clear[3:])

# числа через пробел, вывести в обратном порядке
# порядке
# nums_str = input().split()
# map_list = list(map(int, nums_str))
# map_list.reverse()
# # print(map_list[::-1])
# print(map_list)

matrix = [
    [0, 1, 3],
    [4, 5, 7],
    [10, 2, 19]
]

# print(sum(matrix[1]))
# print(sum(matrix[0]) + sum(matrix[1]) + sum(matrix[2])) 2 1

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(f"matrix[{i}][{j}] = {matrix[i][j]}")
matrix[2].pop(1)
matrix[2].insert(1, 20)
print(matrix)