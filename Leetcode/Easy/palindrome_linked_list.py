'''
Leetcode URL: https://leetcode.com/problems/palindrome-linked-list/
Problem: Palindrome Linked List, 234
Level: Easy
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def show_liked_list(head: ListNode) -> None:
            while head:
                print(head.val)
                head = head.next

        rev = None
        slow = fast = head
        # use Runner to make reverse linked list
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        

        #show_liked_list(fast)
        #show_liked_list(slow)
        #show_liked_list(rev)
    
        # is Palindrome?
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev


sol = Solution()

# TEST
# Input: head = [1,2,2,1]
# Output: true

# Input: head = [1,2,3,2,1]
# Output: true

head = None
head1 = [1,2,2,1]
head2 = [1,2,3,2,1]
for elem in head2:
    if head is None:
        head = ListNode(elem, None)
    else:
        head = ListNode(elem, head)

print(sol.isPalindrome(head))