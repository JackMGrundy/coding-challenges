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
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
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
        
        return cur
                
# 2nd attempt: iterative. 100th percnetile in speed Space: about 12.7MB.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: 
            return head
        cur = None
        stash = head
        
        while stash:
            runner = stash
            stash = stash.next
            runner.next = cur
            cur = runner
        
        return cur


# 3rd attempt: recursive. 100th percentile in speed. 17.7 MB. 
class Solution(object):
    #  Start with helper(None, head)
    def helper(self, leader, lagger=None):
        
        if not leader:
            return lagger

        stash = leader.next
        leader.next = lagger
        return self.helper(stash, leader)
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """   
        return self.helper(head)


if __name__=='__main__':
    head = ListNode(1)
    temp = head
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next

    s = Solution()
    res = s.reverseList(head)
    
    while res:
        print(res.val)
        res = res.next


"""
Notes:

For the recursive solution:
At each level, save head's next and then make head point to the previous node instead. 
Spin up the next level. 
The stopping condition is when head is null. 
The only thing that isn't completely intuitive is the return. Note that at every level
we are returning the result of the level below it. And because the bottom level occurs
when head is null and previous is the original end (now new start) of the list, we will
ultimately return the new start of the list. 

"""