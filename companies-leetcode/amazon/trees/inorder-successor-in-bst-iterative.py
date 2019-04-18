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
        runner = root
        follow = None
    
        while runner:
            if p.val < runner.val:
                follow = runner.val
                runner = runner.left
            else:
                runner = runner.right
        return(follow)


            
        