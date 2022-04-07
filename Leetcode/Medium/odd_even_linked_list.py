'''
Leetcode URL: https://leetcode.com/problems/odd-even-linked-list/
Problem: Odd Even Linked List, 328
Level: Medium
'''
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h_root = head
        t_root = tail = ListNode(None)
        if head is None:
            return head
        while head and head.next:
            tail.next = head.next
            tail = tail.next
            head.next = head.next.next
            
            if head.next:
                head = head.next
            else:
                head.next = t_root.next
                return h_root
            
            tail.next = None

        head.next = t_root.next
        return h_root
    
    # python algorithm interview
    def oddEvenListPAI(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # expection handling
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # while loop, odd,even node changing process
        while even and even.next:
            # odd.next = odd.next.next
            # odd = odd.next
            # even.next = even.next.next
            # even = even.next
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # connect the last odd node and head of even node
        odd.next = even_head
        return head

#sol
sol = Solution()

l1 = [1,2,3,4]

def list_to_ListNode(input_list: list) -> ListNode:
    root = head = ListNode(None)
    for elem in input_list:
        temp = ListNode(elem, None)
        head.next = temp
        head = head.next
    return root.next

head1 = list_to_ListNode(l1)
ret = sol.oddEvenList(head1)
while ret:
    print(ret.val)
    ret = ret.next
