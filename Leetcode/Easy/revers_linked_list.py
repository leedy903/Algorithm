'''
Leetcode URL: https://leetcode.com/problems/reserve-linked-list/
Problem: Reverse Linked List, 206
Level: Easy
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse_list = None
        while head:
            if reverse_list is None:
                reverse_list = ListNode(head.val, None)
            else:
                reverse_list = ListNode(head.val, reverse_list)
            head = head.next
        return reverse_list