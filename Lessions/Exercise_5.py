"""
Дан стек. Необходимо перевернуть его содержимое так, чтобы верхний элемент
стал нижним, а нижний — верхним.
"""

stack = [1, 2, 3, 4, 5, 6, 7]

def stack_reverse(stack: list):
    stack.reverse()
    print(stack)

stack_reverse(stack)