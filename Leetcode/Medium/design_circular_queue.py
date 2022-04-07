'''
Leetcode URL: https://leetcode.com/problems/design-circular-queue/
Problem: Design Circular Queue, 622
Level: Medium
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_len = k + 1
        self.q = [None] * self.max_len
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1)%self.max_len
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.head] = None
        self.head = (self.head + 1)%self.max_len
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail-1)%self.max_len]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail + 1)%self.max_len == self.head

class MyCircularQueuePAI:

    def __init__(self, k: int):
        self.q = [None]*k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# sol
k = 1
obj = MyCircularQueuePAI(k)
param_1 = obj.enQueue(10)
param_6 = obj.isFull()
param_3 = obj.Front()
param_4 = obj.Rear()
param_2 = obj.deQueue()
param_5 = obj.isEmpty()
print(param_1,param_2,param_3,param_4,param_5,param_6)

