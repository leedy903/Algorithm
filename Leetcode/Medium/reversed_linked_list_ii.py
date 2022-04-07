'''
Leetcode URL: https://leetcode.com/problems/reverse-linked-list-ii/
Problem: Reverse Linked List II, 92
Level: Medium
'''
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from Utils import TestHelper as th
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = ListNode(None)
        start.next = head
        count = 1
        reversedNode = None
        while count != left:
            start = start.next
            count = count +1

        end = start.next

        while count != right +1:
            if reversedNode is None:
                tail = reversedNode = ListNode(end.val, None)
            else:
                reversedNode = ListNode(end.val, reversedNode)
            
            end = end.next
            count = count +1
        
        if left == 1:
            head = reversedNode
        else:
            start.next = reversedNode
        tail.next = end

        return head
    
    # python algorithm interview
    def reverseBetweenPAI(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # exception handling
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # change the node's order
        for _ in range(right - left):
            # tmp = start.next
            # start.next = end.next
            # end.next = end.next.next
            # start.next.next = tmp
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next

#sol
sol = Solution()

l1 = [3,5]
l2 = [1,2,3,4,5]

head1 = th.list_to_ListNode(l1)
head2 = th.list_to_ListNode(l2)

ans1 = sol.reverseBetween(head1, 1, 2)
ans2 = sol.reverseBetween(head2, 2, 4)

th.showTest(l1, ans1)
th.showTest(l2, ans2)