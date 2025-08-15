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

components_of_string = ["(", "{", "[", ")", "}", "]"]

# print(ord("(")) - 40
# print(ord("{")) - 123
# print(ord("[")) - 91
# print(ord(")")) - 41
# print(ord("}")) - 125
# print(ord("]")) - 93

# s = input("Введите строку, состоящую из допустимых символов: ")
s = "[]"

class PersonalError(Exception):
    pass

if len(s) > 1:
    for char in s:
        if char in components_of_string:
            if char in components_of_string[0:3]:
                if len(s) % 2 == 0:
                    if len(s) == 2 and (ord(s[0]) == (ord(s[-1]) + 2 or 1)): # ? как сделать привязку к первому символу?
                        print(True)
                        break
                        # if len(s) > 2 - как определить порядок скобок
                    else:
                        print(False)
                else:
                    raise PersonalError("Your len of string must be even!")
            else:
                print(False)

        else:
            raise PersonalError("Your string have incorrect character!")
else:
    raise PersonalError("Your string must contains 2 and more characters!")

# Может попробовать решить через словари?...

