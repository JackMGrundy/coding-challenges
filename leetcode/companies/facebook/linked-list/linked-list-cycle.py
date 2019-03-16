"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""
# Attempt 1: 99th percentile. Main takeaway. For some reason, it's so much faster to use return instead of
# return(). I like the latter syntax and have been using it, but it looks like a lot of my other submissions
# have been much faster than I thought if not for this difference.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        fast = head.next
        slow = head
        
        while fast:
            if fast == slow: return True
            if not fast.next: 
                return False
            
            # Move fast two spots forwards
            fast = fast.next.next
        
            # Move slow forwards 1 spot
            slow = slow.next
        
        return False
        