"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Attempt 1: recursive. 86th percentile

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root==None: return(0)
        longestPath = 0
        
        def helper(node):
            nonlocal longestPath
            l = 0;   r = 0
            
            if node.left:
                l = helper(node.left) + 1
            
            if node.right:
                r = helper(node.right) + 1
            
            if l+r > longestPath:
                longestPath = l+r
            
            if not node.left and not node.right:
                return(0)
            else:
                return(max(l, r))
        
        helper(root)
        return(longestPath)
        
        
        
        