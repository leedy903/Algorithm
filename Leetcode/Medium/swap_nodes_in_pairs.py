'''
Leetcode URL: https://leetcode.com/problems/swap-nodes-in-pairs/
Problem: Swap Nodes in Pairs, 24
Level: Medium
'''
from typing import Optional
'''
Optional[...] is a shorthand notation for Union[..., None] telling the type checker that
either an object of the specific type is required or None is required.
There is technically no difference between using Optional[] on a Union[], or just adding None to the Union[].
So Optional[Union[str, int]] and Union[str, int, None] are exactly same thing.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # sol1: while loop
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            n = head.next
            head.next = n.next
            n.next = head
            
            prev.next = n
            head = head.next
            prev = prev.next.next
        return root.next
    
    # sol2: recursion
    def swapPairsRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            n = head.next
            head.next = self.swapPairsRecur(n.next)
            n.next = head
            return n
        return head