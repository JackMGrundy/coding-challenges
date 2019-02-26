"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# 1st attempt: iterative. 100th percentile in speed. Space: about 12.8MB. Best is 12.5MB.  

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = None
        stash = head
        
        while stash:
            runner = stash
            stash = stash.next
            runner.next = cur
            cur = runner
        
        return(cur)
                
# 2nd attempt: iterative. 100th percnetile in speed Space: about 12.7MB.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return(head)
        cur = None
        stash = head
        
        while stash:
            runner = stash
            stash = stash.next
            runner.next = cur
            cur = runner
        
        return(cur)

# 3rd attempt: recursive. 
        
        