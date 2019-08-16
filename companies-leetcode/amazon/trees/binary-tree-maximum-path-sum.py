"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# 1st attempt: 98th percentile. 88ms.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        def helper(root):
            
            if not root.left and not root.right:
                return (root.val, root.val)
            
            leftsTotalValue, leftsBestBranch = helper(root.left) if root.left else (-float("inf"), -float("inf"))
            rightsTotalValue, rightsBestBranch = helper(root.right) if root.right else (-float("inf"), -float("inf"))
            
            rootsBestBranch = max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch)
            rootsTotalValue = max(root.val,                  \
                                  root.val + leftsBestBranch, \
                                  root.val + rightsBestBranch, \
                                  root.val + leftsBestBranch + rightsBestBranch)
            
            bestTotalValue = max(leftsTotalValue, rightsTotalValue, rootsTotalValue)
            
            return (bestTotalValue, rootsBestBranch)
        
        res, _ = helper(root)
        return res
            
            

# 2nd attempt. same speed as before...98th percentile. 88ms....surprised...have had performance hits with nonlocal before
# clean up with nonlocal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        bestPathValue = -float("inf")
        
        def helper(root):
            nonlocal bestPathValue
            
            if not root.left and not root.right:
                bestPathValue = max(bestPathValue, root.val)
                return root.val
            
            leftsBestBranch = helper(root.left) if root.left else -float("inf")
            rightsBestBranch = helper(root.right) if root.right else -float("inf")
            rootsBestBranch = max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch)
                                         
            bestPathValue =   max(bestPathValue,             \
                                  rootsBestBranch,            \
                                  root.val + leftsBestBranch + rightsBestBranch)
            
            return rootsBestBranch
        
        helper(root)
        return bestPathValue
            



# 3rd attempt. 98th percentile. 88ms. Cleaner.
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        bestPathValue = -float("inf")
        
        def helper(root):
            nonlocal bestPathValue
            
            if not root:
                return 0
            
            leftsBestBranch = helper(root.left)
            rightsBestBranch = helper(root.right)
            rootsBestBranch = max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch)
                                         
            bestPathValue =   max(bestPathValue,             \
                                  rootsBestBranch,            \
                                  root.val + leftsBestBranch + rightsBestBranch)
            
            return rootsBestBranch
        
        helper(root)
        return bestPathValue