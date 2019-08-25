"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Iterative.
# 32ms. 95th percentile
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        nodeBeforeSwapSection = dummy
        
        while head and head.next:
            headsOldNext = head.next
            nodeBeforeSwapSection.next = headsOldNext
            head.next, headsOldNext.next = headsOldNext.next, head
            nodeBeforeSwapSection, head = head, head.next
        
        return dummy.next
        
        

# Recursive
# 32ms. 95th percentile.
# I really like this method...elegant
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextSectionHead = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(nextSectionHead)
        return head