'''
Leetcode URL: https://leetcode.com/problems/implement-queue-using-stacks/
Problem: Implement Queue using Stacks, 232
Level: Easy
'''
from collections import deque
class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.output.pop()
        

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self) -> bool:
        return self.input == [] and self.output == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# sol
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek(), obj.pop(), obj.empty())