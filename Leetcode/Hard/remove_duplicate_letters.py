'''
Leetcode URL: https://leetcode.com/problems/remove-duplicate-letters/
Problem: Remove Duplicate Letters, 316
Level: Hard
'''
from collections import Counter


class Solution:
    def removeDuplicateLetters (self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)

# sol
sol = Solution()

#s1 = "bcabc"
s2 = "cbacdcbc"

#print(sol.removeDuplicateLetters(s1))
print(sol.removeDuplicateLetters(s2))