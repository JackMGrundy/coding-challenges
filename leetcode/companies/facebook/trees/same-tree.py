"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
# First attempt: 100th percentile in speed. 85th percentile in space at about 10.7MB
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bfs(self, root):
        q = deque([root])
        res = []
        
        while q:
            cur = q.popleft()
            if cur==None:
                res.append("None")
            else:
                res.append(cur.val)
                for c in [cur.left, cur.right]:
                    q.append(c)
        return(res)
                
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pStr = self.bfs(p)
        qStr = self.bfs(q)
        return(pStr==qStr)




# Second attempt: 99th percentile in speed. 92th percentile in space...10.6MB in space...shorter
class Solution(object):
                
        
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p, q) == (None, None):
            return(True)
        elif p and q:
            return( p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) ) 
        else:
            return(False)
        