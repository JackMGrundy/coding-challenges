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
        vals = { root: root.val };  stack = [root];   res = 0
        
        while stack:
            curNode = stack.pop()
            if (curNode.right==None) and (curNode.left==None):
                res += vals[curNode]
            
            for c in [curNode.left, curNode.right]:
                if c:
                    vals[c] = 10*vals[curNode] + c.val
                    stack.append(c)
        return(res)