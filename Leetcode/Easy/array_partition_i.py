'''
Leetcode URL: https://leetcode.com/problems/array-partition/
Problem: Array Partition, 561
Level: Easy
'''
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if i%2 == 0:
                ans += nums[i]
        return ans

sol = Solution()
# TEST
test_inputs = [
                # Output: 4
                [1,4,3,2],
                # Output: 9
                [6,2,6,5,1,2]
            ]

for test_input in test_inputs:
    print(sol.arrayPairSum(test_input))