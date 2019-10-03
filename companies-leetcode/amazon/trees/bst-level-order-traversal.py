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
# 32ms. 99 percentile.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        depth = -1
        res = []
        level = []
        
        while q:
            node, nodeDepth = q.popleft()
            
            if depth < nodeDepth:
                res.append(level)
                level = []
                depth += 1
            
            level.append(node.val)
            
            for c in [node.left, node.right]:
                if c:
                    q.append( (c, nodeDepth + 1) )
        
        res.append(level)
        
        return res[1:]