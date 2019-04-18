"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# 1st attempt: 42nd percentile in speed. Recursive
"""
Intuition:
At each node, we want the maxDepth in both the left and right subtress. If they differ by more than 1, we
return false. This implementation continues searching for mismatches even after finding 1. Will improve
this in next attempt. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        res = True
        
        def helper(node, d):
            nonlocal res
            if not node: 
                return d
            
            lD = helper(node.left, d+1)
            rD = helper(node.right, d+1)
            
            if abs( lD - rD ) > 1:
                res = False
            
            return max(lD, rD)
            
        helper(root, 1)
        return res

# 2nd attempt: 92nd percentile in speed.
"""
Turns out that changing the nonlocal var to a class variable was enough to get a ton of speedup
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        
        def helper(node, d):
            if not node: 
                return d
            
            lD = helper(node.left, d+1)
            rD = helper(node.right, d+1)
            
            if abs( lD - rD ) > 1:
                self.res = False
            
            return max(lD, rD)
            
        helper(root, 1)
        return self.res