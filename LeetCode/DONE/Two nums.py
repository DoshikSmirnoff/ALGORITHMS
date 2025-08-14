"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

array_nums = [2, 7, 6, 11, 15]
target = 9
indexes = []

sorted_list = [num for num in array_nums if num <= target]

for i_index, i in enumerate(sorted_list):
    for j_index, j in enumerate(sorted_list):
        if i + j == target:
            indexes = [i_index, j_index]
            break
        else:
            break

print(indexes)

# Здесь надо переписать решение в виде класса и загрузить в литкод
