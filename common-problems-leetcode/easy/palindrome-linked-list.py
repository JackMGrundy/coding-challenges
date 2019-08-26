"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# 68ms. 98th percentile.
# Shouldn't be classified as an easy problem.
# The best solution involves reversing a subsection of the list.
# That process alone is a separate problem that's labeled medium difficulty. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        listLen = 0
        runner = head
        while runner:
            listLen += 1
            runner = runner.next
        previous = head
        current = previous.next
        nextNode = None if not current else current.next 
        for _ in range(listLen//2 - 1):
            current.next = previous
            previous = current
            current = nextNode
            nextNode = current.next
        firstHalfHead = previous
        secondHalfHead = current if listLen % 2 == 0 else nextNode
        
        while firstHalfHead and secondHalfHead:
            if firstHalfHead.val != secondHalfHead.val:
                return False
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        
        return True