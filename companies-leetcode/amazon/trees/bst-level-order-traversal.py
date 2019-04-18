"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque

class TreeNode:
    def __init__(self, num):
        self.val = num
        self.right = None
        self.left = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return([])
        res = [];  curLevelNodes = [];  curLvl = 0
        queue = deque()
        queue.append((root, curLvl))
        while queue:
            curNode, curNodeLvl = queue.popleft()
            if curNodeLvl != curLvl:
                res.append(curLevelNodes)
                curLevelNodes = []
                curLvl = curNodeLvl
            curLevelNodes.append(curNode.val)
            for c in [curNode.left, curNode.right]:
                if c is not None: 
                    queue.append((c, 1+curLvl))
        res.append(curLevelNodes)
        return(res)