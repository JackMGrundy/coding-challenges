# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #Edge case
        if not root: return True
        
        stack = []; minValue = -float('inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
                if node: 
                    if node.val <= minValue: return(False)
                    minValue = node.val
        return True