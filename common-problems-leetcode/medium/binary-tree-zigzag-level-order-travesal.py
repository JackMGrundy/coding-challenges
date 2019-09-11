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
# 38ms. 90 percentile. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        
        queue = collections.deque([(root, 0)])
        level = 0
        order = 1
        curLevelValues = []
        res = []
        
        while queue:
            cur, curLevel = queue.popleft()
            if level < curLevel:
                level += 1
                res.append(curLevelValues[::order])
                curLevelValues = []
                order *= -1
            
            curLevelValues.append(cur.val)
            
            for c in [cur.left, cur.right]:
                if c:
                    queue.append( (c, curLevel + 1) )
        
        res.append(curLevelValues[::order])
        
        return res
        
        