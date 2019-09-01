"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
Accepted
201,935
Submissions
547,333
"""

# 224ms. 77 percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)
    
    def merge(self, l1, l2) -> ListNode:
        head = ListNode(-1)
        temp = head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
        
        return head.next
        
        
        
"""
Notes:
This is O(log(N)) space. To get it to constant space, you'd have to do iterative/bottom up
merge sort. 

Note the prev.next = null line to break apart the two component lists...
"""