'''
Leetcode URL: https://leetcode.com/problems/implement-stack-using-queues/
Problem: Implement Stack using Queues, 225
Level: Easy
'''
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# sol
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top(), obj.pop(), obj.empty())