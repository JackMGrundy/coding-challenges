# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return(0)
        res = 0
        def dfs(curNode, num):
            nonlocal res
            if (curNode.left == None) and (curNode.right == None):
                res += 10*num + curNode.val
                return
            if curNode.left:
                dfs(curNode.left, num*10+curNode.val)
            if curNode.right:
                dfs(curNode.right, num*10+curNode.val)
        
        dfs(root, 0)
        return(res)       