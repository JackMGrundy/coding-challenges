"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /   
1

Output: null
"""
class TreeNode:
    def __init__(self, num):
        self.val = num
        self.right = None
        self.left = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root: return(None)
        res = []
        
        def dfs(curNode, res):
            if curNode is None: 
                return
            dfs(curNode.left, res)
            res.append(curNode.val)
            dfs(curNode.right, res)
        
        dfs(root, res)
        
        for counter, val in enumerate(res):
            if val==p.val and counter < len(res)-1: return(res[counter+1])
        
        return(None)