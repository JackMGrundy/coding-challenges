"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# 48ms. 68th percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        res = deleter = ListNode(-1)
        deleter.next = head
        
        while deleter and deleter.next and deleter.next.next:

            while deleter.next and deleter.next.next and deleter.next.val == deleter.next.next.val:
                deleteVal = deleter.next.val
                
                while deleter.next and deleter.next.val == deleteVal:
                    deleter.next = deleter.next.next
            
            deleter = deleter.next
        
        return res.next


"""
Notes:

Gotta watch out for the cases where there are back to back duplicates...and there can be of odd or even number of duplicates in each group.

"""