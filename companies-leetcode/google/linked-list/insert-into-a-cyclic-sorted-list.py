"""
Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to that single node. Otherwise, you should return the original given node.

The following example may help you understand the problem better:

 



In the figure above, there is a cyclic sorted list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list.

 



The new node should insert between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
"""
# 94th percentile
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        # Case: the list is empty
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        res = head
        head = head.next
        cur = Node(insertVal, None)
        while True:
            # node equals insertVal
            if head.val == insertVal:
                cur.next, head.next = head.next, cur
                return res
            
            # insertVal should go in the "middle" of the list
            if head.val < insertVal and head.next.val >= insertVal:
                cur.next, head.next = head.next, cur
                return res
            
            # insertVal should go at the "beginning" of the list
            if head.val > head.next.val > insertVal:
                cur.next, head.next = head.next, cur
                return res
            
            # insertVal should go at the "end" of the list
            if insertVal > head.val > head.next.val:
                cur.next, head.next = head.next, cur
                return res
            
            # we hit the beginning again and did not find a place to
            # put the value on the first go. Insert anywhere.
            if res == head:
                cur.next, head.next = head.next, cur
                return res
            
            head = head.next