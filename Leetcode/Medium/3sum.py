'''
Leetcode URL: https://leetcode.com/problems/3sum/
Problem: 3Sum, 15
Level: Medium
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 2:
            return []

        neg_num = 0
        pos_num = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= 0:
                neg_num = i
                if nums[i] == 0:
                    pos_num = len(nums) - neg_num -1
                break

        # print("\ncount:", pos_num, neg_num)
        # print("LEFT\t RIGHT")

        sum_lists = []
        # [-4, -1, -1, 0, 1, 2]
        left, right = 0, len(nums)-1
        while left < right and nums[left] <= 0 and nums[right] >= 0:
            # print("{}\t {}".format(left, right))

            remain = -(nums[left] + nums[right])
            if remain in nums[left+1:right]:
                sum_list = [nums[left], remain, nums[right]]
                if sum_list not in sum_lists:
                    sum_lists.append(sum_list)
            if remain > 0:
                left += 1
            elif remain < 0:
                right -= 1
            else:
                if pos_num - (len(nums)-right) > neg_num - (left + 1):
                    right -=1
                else:
                    left += 1

        return sum_lists

    # brute force
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        # brute force n^3 repeat
        for i in range(len(nums) - 2):
            # skip the repeated value
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums [k - 1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        return results
    
    # two pointers
    def threeSum3(self, nums: list[int]) -> list[list[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # skip the repeated value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # reduce the distance between left and right and calculate the sum
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1

        return results

sol = Solution()

# TEST
test_inputs = [
                 # Output: [[-1,-1,2],[-1,0,1]]
                [-1,0,1,2,-1,-4],
                # Output: []
                [],
                # Output: []
                [0, 0, 0, 0],
                 # Output: [[-2,0,2],[-2,1,1]]
                [-2, 0, 1, 1, 2],
                # Output: [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
                [-1,0,1,2,-1,-4,-2,-3,3,0,4] 
            ]

for test_input in test_inputs:
    # TEST 1
    print(sol.threeSum(test_input))
    # TEST 2
    print(sol.threeSum2(test_input))
    # TEST 3
    print(sol.threeSum3(test_input))