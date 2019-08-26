"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# 64ms. 99th percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1->2->2->2->6->3->2
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        runner = dummy
        
        while runner:
            while runner.next:
                if runner.next.val == val:
                    runner.next = runner.next.next
                else:
                    break
            
            runner = runner.next
        
        return dummy.next