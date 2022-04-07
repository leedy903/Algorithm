'''
Leetcode URL: https://leetcode.com/problems/daily-temperatures/
Problem: Daily Temperatures, 739
Level: Medium
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        return ans


# sol
sol = Solution()

t1 = [73,74,75,71,69,72,76,73]
t2 = [30,40,20,60]
t3 = [30,60,90]

print(sol.dailyTemperatures(t1))
print(sol.dailyTemperatures(t2))
print(sol.dailyTemperatures(t3))