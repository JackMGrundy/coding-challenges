"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
# 1st attempt: 85th percentile in speed. Recursive.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, d):
            if not node: return d
            return(max( helper(node.left, d+1), helper(node.right, d+1) ))
        
        return helper(root, 0)

# 2nd attempt: 53rd percentile. Iterative.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        s = [ (root,0) ]
        res = 0
        while s:
            cur,d = s.pop()
            if not cur:
                res = max(res, d)
            else:
                for c in [cur.right, cur.left]:
                    s.append( (c, d+1) )
        
        return res
                
            
# 3rd attempt: 53rd percentile. Iterative.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        s = [ root ]
        memo = {root: 0}
        res = 0
        while s:
            cur = s.pop()
            if not cur:
                res = max(res, memo[cur])
            else:
                for c in [cur.right, cur.left]:
                    memo[c] = memo[cur]+1
                    s.append(c)
        
        return res
                
            
