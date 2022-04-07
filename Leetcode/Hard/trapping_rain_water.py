'''
Leetcode URL: https://leetcode.com/problems/trapping-rain-water/
Problem: Trapping Rain Water, 42
Level: Hard
'''
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        amount = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                amount += left_max-height[left]
                left += 1
            else:
                amount += right_max-height[right]
                right -= 1
       
        return amount

    # stack
    def trap2(self, height: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다.
                top = stack.pop()
                if not len(stack):
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters
        
            stack.append(i)
        return volume
        
sol = Solution()

# TEST 1
Input1 = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output1 6
# TEST 1.1
print(sol.trap(Input1))
# TEST 1.2
print(sol.trap2(Input1))

# TEST 2
Input2 = [0, 0, 0, 1, 0, 0, 0]
# Output2 0
# TEST 2.1
print(sol.trap(Input2))
# TEST 2.2
print(sol.trap2(Input2))