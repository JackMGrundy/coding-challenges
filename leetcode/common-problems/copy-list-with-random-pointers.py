"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""
# 1st attempt: 100th percentile in speed and space
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        memo = {}
        origRunner = head
        res = newRunner = memo[head] = Node(head.val, None, None)
            
        # Copy nodes
        while origRunner:
            if origRunner.next:
                # Copy the next node
                cpy = Node(origRunner.next.val, None, None)
                memo[origRunner.next] = cpy
                newRunner.next = cpy
            
            origRunner = origRunner.next
            newRunner = newRunner.next
        
        # Deal with random connections
        origRunner = head
        newRunner = res
        while origRunner:
            if origRunner.random:
                newRunner.random = memo[origRunner.random]
            origRunner = origRunner.next
            newRunner = newRunner.next
        
        return res
            
         
        