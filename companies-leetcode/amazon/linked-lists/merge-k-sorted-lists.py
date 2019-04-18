"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
            
        head = runner = ListNode(0)
        for num in sorted(nums):
            runner.next = ListNode(num)
            runner = runner.next

        return(head.next)