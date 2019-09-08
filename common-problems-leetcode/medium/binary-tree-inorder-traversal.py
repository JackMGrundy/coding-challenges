"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Iterative.
# 32ms 93 percentile.
# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            elif stack:
                root = stack.pop()
                res.append(root.val)
                root = root.right

        return res


# Recursive.
# 32ms. 93rd percentile.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(root):
            nonlocal res
            if not root:
                return 
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
            
        
        dfs(root)
        return res