'''
Leetcode URL: https://leetcode.com/problems/merge-two-sorted-lists/
Problem: Merge Two Sorted Lists, 21
Level: Easy
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        merge_list = head
        while l1 or l2:
            if not l1:
                merge_list.next = l2
                break
            elif not l2:
                merge_list.next = l1
                break
            if l1.val < l2.val:
                merge_list.next = l1
                l1 = l1.next
            else:
                merge_list.next = l2
                l2 = l2.next
            merge_list = merge_list.next
                
        return head.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1

sol = Solution()
# TEST 
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

head1 = ListNode()
head2 = ListNode()
l1, l2 = [1,2,4], [1,3,4]

def list_to_ListNode(head: ListNode, input_list: list) -> None:
    for elem in input_list:
        temp = ListNode(elem, None)
        head.next = temp
        head = head.next

def show_liked_list(head: ListNode) -> None:
    while head:
        print(head.val)
        head = head.next

list_to_ListNode(head1, l1)
list_to_ListNode(head2, l2)

# show_liked_list(head1.next)
# show_liked_list(head2.next)
# show_liked_list(sol.mergeTwoLists(head1.next, head2.next))

show_liked_list(sol.mergeTwoLists2(head1.next, head2.next))
