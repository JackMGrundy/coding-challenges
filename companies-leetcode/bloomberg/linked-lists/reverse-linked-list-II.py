"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        nodeBeforeTargetSection = dummy
        for _ in range (1, m):
            nodeBeforeTargetSection = nodeBeforeTargetSection.next
        
        newEndOfTargetSection = nodeBeforeTargetSection.next
        previous = nodeBeforeTargetSection.next
        current = previous.next
        nextNode = None
        for _ in range(n-m):
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        
        nodeBeforeTargetSection.next = previous
        newEndOfTargetSection.next = current
        
        return dummy.next