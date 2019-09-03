"""

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# 84ms. 99.6the percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = fast = previous = res = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next
        
        previous.next = None
        previous = slow
        current = slow.next
        slow.next = None
        after = None

        while current:
            after = current.next
            current.next = previous
            previous = current
            current = after
        
        firstHalfHead = head
        secondHalfHead = previous
            
        while firstHalfHead and secondHalfHead:
            firstHalfHead.next, firstHalfHead = secondHalfHead, firstHalfHead.next
            
            if firstHalfHead:
                secondHalfHead.next, secondHalfHead = firstHalfHead, secondHalfHead.next

        return res
                
        


"""
Notes:
Find the second half of the list. Reverse it. Link by taking the first node from the first half, the first node from
the second, and so on. 
"""