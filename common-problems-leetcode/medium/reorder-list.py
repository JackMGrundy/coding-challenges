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
        if not head:
            return None
        slow = fast = head
        length = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 2
        
        previous = None
        current = slow.next
        slow.next = None
        while current:
            after = current.next
            current.next = previous
            previous = current
            current = after
        
        cap = merger = ListNode(-1)
        while head or previous:
            if head:
                merger.next = head
                merger = merger.next
                head = head.next
            if previous:
                merger.next = previous
                merger = merger.next
                previous = previous.next

        return cap.next
                
        


"""
Notes:
Find the second half of the list. Reverse it. Link by taking the first node from the first half, the first node from
the second, and so on. 
"""