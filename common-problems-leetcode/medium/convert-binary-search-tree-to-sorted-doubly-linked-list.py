"""
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right 
pointers as synonymous to the previous and next pointers in a doubly-linked list.

Let's take the following BST as an example, it may help you understand the problem better:

 


 
We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has 
a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last 
element, and the successor of the last element is the first element.

The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node 
it points to is the smallest element of the linked list.

 


 
Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree 
node should point to its predecessor, and the right pointer should point to its successor. We should return the 
pointer to the first element of the linked list.

The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed 
line means the predecessor relationship.
"""


# Iterative. 
# Making a new list: 696ms. 99 percentile.
# Rearranging old node: 728ms. 68 percentile.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        first, last = None, None
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                node = stack.pop()
                root = node.right
                
                # Uncomment to copy tree instead of relinking
                # node = Node(node.val)
                
                if not first:
                    first = node
                if last:
                    node.left = last
                    last.right = node
                last = node
        
        last.right = first
        first.left = last
        return first
            


# 708ms. 92nd percentile.
# Recursive
class Solution:
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = None
        last = None

        def inorder(root):
            nonlocal first
            nonlocal last
            if not root:
                return None

            inorder(root.left)
            newNode = Node(root.val)
            if not first:
                first = newNode
            if last:
                newNode.left = last
                last.right = newNode
            last = newNode
            inorder(root.right)

        
        inorder(root)
        last.right = first
        first.left = last
        return first

"""
Notes:

"""