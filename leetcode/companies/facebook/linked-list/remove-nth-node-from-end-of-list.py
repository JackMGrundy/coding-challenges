"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Attempt 1: 60th percentile in speed. 2 passes.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return(None)
        res = tempRem = tempLen = head
        
        # Get length
        l = 1
        while tempLen.next:
            l += 1
            tempLen = tempLen.next
        
        # Disconnect
        if l==n: return(head.next)
        steps = l - n - 1
        for i in range(steps):
            tempRem = tempRem.next
        tempRem.next = tempRem.next.next
        
        return(res)

# Attempt 2: 60th percentile in speed. 1 pass but double the space used with a dictionary.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return(None)
        d = {}
        runner = head
        l = 0
        while runner:
            l += 1
            d[l] = runner
            runner = runner.next
        
        target = l - n
        if target==0: return(head.next)
        else:
            d[target].next = d[target+1].next
            return(head)
            
        
            
# Attempt 3: 100th percentile. Technically 1 pass...but seems silly...
# stil advancing two markers. Only a couple ms faster.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return(None)
        fast = slow = prev = head
        
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return(head.next)
        
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        
        prev.next = slow.next
        return(head)