"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = l1.val + l2.val
        carry = 1 if s >= 10 else 0
        s = s % 10
        root = ListNode(s);    runner = root
        l1 = l1.next;          l2 = l2.next

        while l1 or l2:
            s = carry
            if l1: s += l1.val
            if l2: s += l2.val
            carry = 1 if s >= 10 else 0
            s = s % 10
            runner.next = ListNode(s)
            runner = runner.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
    
        if carry: runner.next = ListNode(carry)
        
        return(root)
        
            
            
      