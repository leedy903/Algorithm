'''
Leetcode URL: https://leetcode.com/problems/zigzag-conversion/
Problem: Zigzag Conversion, 6
Level: Medium
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = [[] for _ in range(numRows)]
        i = 0
        IsUp = True
        for char in s:
            zigzag[i].append(char)
            if i == numRows-1:
                IsUp = False
            elif i == 0:
                IsUP = True
            i += 1 if IsUP else -1
  
        ans = ""
        for i in range(numRows):
            ans += zigzag[i]
        return ans

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))