"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Not allowed because nodes don't have next values...but still want to record that you could this with constant space via
# a level order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        
        while root:
            levelStart = TreeNode(-1)
            currentChild = levelStart
            firstInLevel = True
            while root:
                if root.right:
                    currentChild.next = root.right
                    currentChild = currentChild.next
                    if firstInLevel:
                        res.append(currentChild.val)
                        firstInLevel = False
                if root.left:
                    currentChild.next = root.left
                    currentChild = currentChild.next
                    if firstInLevel:
                        res.append(currentChild.val)
                        firstInLevel = False
                root = root.next
            root = levelStart.next

        return res



# 83rd percentile. 36ms. 
# BFS. O(N) space and time
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        level = 1
        curLevel = 0
        queue = deque([(root, level)])
        while queue:
            cur, level = queue.popleft()
            if level > curLevel:
                res.append(cur.val)
                curLevel = level
            for c in [cur.right, cur.left]:
                if c:
                    queue.append( (c, level+1) )

        return res