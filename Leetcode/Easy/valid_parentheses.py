'''
Leetcode URL: https://leetcode.com/problems/valid-parentheses/
Problem: Valid Parentheses, 20
Level: Easy
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for elem in s:
            if elem == '(' or elem == '{' or elem == '[':
                stack.append(elem)
            elif not stack:
                return False
            elif elem == ')' and '(' != stack.pop():
                return False
            elif elem == '}' and '{' != stack.pop():
                return False
            elif elem == ']' and '[' != stack.pop():
                return False
            
        return not len(stack)
    def isValidPAI(self, s: str) -> bool:
        stack = []
        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['            
        }
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0