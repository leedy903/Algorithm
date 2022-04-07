'''
Leetcode URL: https://leetcode.com/problems/product-of-array-except-self/
Problem: Product Of Array Except Self, 238
Level: Medium
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        p = 1
        for n in nums:
            product.append(p)
            p *= n
            
        p = 1
        for i in range(len(nums) -1, -1, -1):
            product[i] *= p
            p *= nums[i]
        return product