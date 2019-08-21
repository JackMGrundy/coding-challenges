"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# 72ms. 97th percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1Num = 0
        while l1:
            l1Num = l1Num*10 + l1.val
            l1 = l1.next
        
        l2Num = 0
        while l2:
            l2Num = l2Num*10 + l2.val
            l2 = l2.next
        
        l1Plusl2 = l1Num + l2Num
        head = ListNode( l1Plusl2 % 10 )
        l1Plusl2 = l1Plusl2 // 10
        
        while l1Plusl2:
            temp = ListNode( l1Plusl2 % 10 )
            l1Plusl2 = l1Plusl2 // 10
            temp.next = head
            head = temp
        
        return head
            