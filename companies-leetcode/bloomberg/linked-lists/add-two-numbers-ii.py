"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""
# 64ms. 99.8 percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
d -> 9 -> 9 -> 9
d -> 1 -> 1 -> 1
   
1 -> 1 -> 0 -> 0


"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Value, l2Value = 0, 0
        while l1:
            l1Value = l1Value*10 + l1.val
            l1 = l1.next
        while l2:
            l2Value = l2Value*10 + l2.val
            l2 = l2.next
        total = l1Value + l2Value
        if total == 0:
            return ListNode(0)
        
        head = None
        while total:
            nextDigit = total % 10
            total = total // 10
            temp = ListNode(nextDigit)
            temp.next = head
            head = temp
        
        return head

"""
Notes:

Simply find the two numbers the lists represent them, add them, construct the output list one digit at a time.
"""