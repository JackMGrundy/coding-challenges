"""
Given  a  singly  linked list, group all odd nodes together followed by the even
nodes.  Please  note here we are talking about the node number and not the value
in the nodes.                                                                   

You  should  try  to  do  it  in  place.  The  program  should run in O(1) space
complexity and O(nodes) time complexity.                                        

Example 1:                                                                      

Input: 1->2->3->4->5->NULL                                                      

Output: 1->3->5->2->4->NULL                                                     

Example 2:                                                                      

Input: 2->1->3->5->6->4->7->NULL                                                

Output: 2->3->6->7->1->5->4->NULL                                               

Note:                                                                           

The  relative  order inside both the even and odd groups should remain as it was
in the input.                                                                   

The first node is considered odd, the second node even and so on ...            

"""

# 44ms. 94 percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        oddCap = A = head
        evenCap = B = head.next
        isAOdd = True
        
        while A and B:
            if not B.next and isAOdd:
                break
            
            A.next = B.next
            A, B = B, A.next
            isAOdd = not isAOdd

        A.next = evenCap
        return oddCap

"""
Notes:

We have two pointers, A and B, initially set to the first and second elements of the list.
We want to change A.next to equal B.next. Then we can update A to hold B and B to hold B.next.

An example:
1->2->3->4->5->NULL

A = 1
B = 2

We make A.next = 3 and then update for the next round with
A = 2
B = 3

This simple linking will provide the two lists we need, one that starts at the first node in the list
and one that starts at the second.

The only wrinkly is how to combine them. The while loop will terminate when B is none and A
isn't. If A is the last odd value, we can just make its next the even list and we're done.
If it A is the last even, we're stuck though. To avoid that, we look ahead in each loop 
to see if A and B are the last two nodes. If they are and A is odd, then there's no need for
more linking (we would just make A's next equal to B's next = None), and we can break there
so that we know A holds the last odd. 

"""