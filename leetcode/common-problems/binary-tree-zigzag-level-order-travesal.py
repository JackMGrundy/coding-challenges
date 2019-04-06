"""

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# 1st attempt: 75th percentile in speed
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        curLevel = 1
        curList = [ ]
        res = [ ]
        q = deque([ (root, 1) ])
        order = 1
        
        while q:
            cur,d = q.popleft()
            if d > curLevel:
                curList = curList[::order]
                res.append(curList)
                curList = []
                curLevel += 1
                order *= -1
            if cur:
                curList.append(cur.val)
                for c in [ cur.left, cur.right ]:
                    q.append( (c, d+1) )
        
        return res

# 2nd attempt: 99th percentile in speed (I think this is just due to inconsistent timing...very small absolute difference)
"""
Not much faster, but cleaner and interesting phrasing...
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res
        
        order = 1
        s = deque([root])
        
        while s:
            level = []
            
            for _ in range(len(s)):
                cur = s.popleft()
                
                level.append(cur.val)
                
                if cur.left: s.append(cur.left)
                if cur.right: s.append(cur.right)
            
            if level:
                res.append(level[::order])
            
            order *= -1
        
        return res
        
        