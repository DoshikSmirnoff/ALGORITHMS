"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

s = "hbg"
t = "ahbgdc"
result = ""
indexes_chars = []

for i in s:
    if i in t:
        result += i
        indexes_chars.append(t.index(i))

if len(result) == len(s):
    if indexes_chars == sorted(indexes_chars):
        # print(result)
        # print(indexes_chars)
        print(True)
    else:
        print(False)
else:
    print(False)

# Здесь надо переписать решение в виде класса и загрузить в литкод