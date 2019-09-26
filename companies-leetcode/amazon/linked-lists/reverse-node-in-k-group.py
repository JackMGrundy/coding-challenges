"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a 
multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# 52ms. 89 percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2 or not head:
            return head
        
        runner, length = head, 0
        while runner:
            length, runner = length + 1, runner.next
        
        res = current = ListNode(-1)
        res.next = head
        for _ in range(length // k):
            current = self._reverseKNodes(current, k)
        return res.next
    
    def _reverseKNodes(self, nodeBeforeGroup, k):
        previous, current, after = nodeBeforeGroup, nodeBeforeGroup.next, None
        newEndOfGroup = current
        while current and k != 0:
            after = current.next
            current.next = previous
            previous = current
            current = after
            k -= 1
        
        nodeBeforeGroup.next = previous
        newEndOfGroup.next = current
        return newEndOfGroup


"""
Notes:
When you reverse a linkedlist, you can initialize previous to None and make the first node point back to it. This is a little
bit different, because we need to keep track of the node before the group we're reversing so that we can make the end
of the reversed section point back to it.

Also, as far as I can tell, there is no way to avoid going over the list twice. You only want to reverse a section if
there are enough nodes to complete a full section. This implies that you have to look ahead k nodes befoe doing a reversal.
Or equivalently, count all the nodes at the beginning. 
"""