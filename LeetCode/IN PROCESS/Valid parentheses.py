"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
3) Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false
"""

def check_correct(string: str) -> bool:
    stack = []
    for char in string:
        if char in dict_of_string:  # открывающая скобка
            stack.append(char)
        else:  # закрывающая скобка
            if not stack:  # нет открытой скобки для закрытия
                return False
            last_open = stack.pop()
            if dict_of_string[last_open] != char:
                return False
    return not stack  # стек должен быть пустым

