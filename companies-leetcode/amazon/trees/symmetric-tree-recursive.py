# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def symmetric(s):
    print(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: return(False)
    return(True)

class Solution:    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return(True)
        
        def equate(node, sibling):
            if node is None and sibling is None: return(True)
            if node is None or sibling is None: return(False)
            return( equate(node.left, sibling.right) and (node.val==sibling.val) and equate(node.right, sibling.left)   )
        
        return(equate(root.left, root.right))