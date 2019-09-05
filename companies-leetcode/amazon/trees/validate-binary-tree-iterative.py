"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
 Iterative pre-order search
 The stack is like what you would have implicitly in memory with a recursive approach. As in pre-order travesal,
 iterate all the way to the left as far as you can. Then pop off a node. Process it, and then add go left as far
 as you can adding those nodes to the stack along the way.

 Last thing to note is the "processing" done to actually solve the problem. The logic is pretty elegant. Pre order
 traversal traveses the graph from left to right, which should be a strictly increasing sequence for a BST. Therefore,
 when evaluating a node, we don't have to evaluate if it is less than any nodes to the right...all we have to do
 is make sure it's greater than the "farthest" right value" we have seen so far. 
"""

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Edge case
        if not root: 
            return True
        
        stack = []; minValue = -float('inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right  #Key line
                if node: 
                    if node.val <= minValue: 
                        return False
                    minValue = node.val
        return True

    


# Python 3: 75th percentile. 52 ms.
# Recursive...just keep track of the "window" created by the parent and either the largest ancestor to the left or the
# smallest ancestor to the right.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, largestLeftAncestor, smallestRightAncestor) -> bool:
            if not root:
                return True
        
            if root.left and not (largestLeftAncestor < root.left.val < root.val):
                return False
            
            if root.right and not (root.val < root.right.val < smallestRightAncestor):
                return False
            
            return helper(root.left, largestLeftAncestor, root.val) and helper(root.right, root.val, smallestRightAncestor)
        
        return helper(root, -float("infinity"), float("infinity"))