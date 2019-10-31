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
# 2 passes. 100th percentile in speed and space. 36ms. 
# The first pass deep copies the nodes and their normal connections. It makes each new
# node's random pointer point to the corresponding old copy. 
#  The first pass makes a memo mapping old nodes to their copies.
# Given this memo, we make a second pass and change each random pointer - pointing to old node - to point
# towards the corresponding new node via the memo
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
        res = randomLinker = normalLinker = Node(head.val, head.next, head.random)
        memo = {head : res}
        
        # Link normal nodes
        while head.next:
            copyOfNext = Node(head.next.val, head.next.next, head.next.random)
            normalLinker.next = copyOfNext
            
            memo[head.next] = copyOfNext
            head = head.next
            normalLinker = normalLinker.next
        
        # Link random nodes
        while randomLinker:
            if randomLinker.random:
                randomLinker.random = memo[randomLinker.random]
            randomLinker = randomLinker.next
        
        return res


# One pass. 36ms. 99.75 percentile.
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
        oldToNew = {}
        
        cap = copy = Node(None, None, None)
        
        while head:
            if head in oldToNew:
                newNode = oldToNew[head]
            else:
                newNode = Node(head.val, None, None)
                oldToNew[head] = newNode
            
            randomNode = None
            if head.random in oldToNew:
                randomNode = oldToNew[head.random]
            elif head.random:
                randomNode = Node(head.random.val, None, None)
                oldToNew[head.random] = randomNode
            
            copy.next = newNode
            copy.next.random = randomNode
            copy = copy.next
            head = head.next
        
        return cap.next



# Attempt 3: 44ms. 92nd percentile
"""
A very cool resursive solution. The intuition:
We keep a dictionary mapping old nodes to new copies
Each recursive call checks if we've already copied the passed in node. If we have, just return the already made copy
Otherwise, make a copy of it and remember. 
Now for the cool part:
For the copy's next node, we recursively call the function on the original node's next. 
When we make the "nexts" we're passing through the list for the first time, so inside that recursive call, there
is no way we have already copied the node before. So we'll just copy the node, remember it, and then hit
another recursive call to copy that node's next. We do this all the way to the end of the chaing.

Then, in the recursive call for the very last node, we can proceed to the call to connect the node's random pointer.
At this point, we've seen all the nodes, so when we make a recursive call to connect its random pointer, it'll stop
at the "have we seen this before" part and just return the already made copy. Finally, the recursive call for the very
last node returns a reference to the very last node to the call for the second to last node. Which in turn links
its random node and so on...

So this basically goes through the node forwards to take care of the main connections and then it goes backwards
through the list for the random connections. 

The result is very clean and precise.

Downsides are the stack could get large if the chain is long...typical recursive problem...and I'd still opt
for the iterative solution as it's easy to understand. 
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.copied = {}
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: 
            return None
        if head in self.copied:
            return self.copied[head]
        else:
            newNode = Node(head.val, None, None)
            self.copied[head] = newNode
            newNode.next = self.copyRandomList(head.next)
            newNode.random = self.copyRandomList(head.random)
        return newNode