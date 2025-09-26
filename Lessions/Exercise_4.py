"""
Дан стек.
Необходимо удалить из него все отрицательные элементы.
"""

def stack(arr):

  for num in arr:
    if num >=0:
      print(num)

arr = [3, -1, 5, -7, 2, -4, 8]

stack(arr)