# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closestValue = root.val
        while root:
            if abs(target - root.val) < abs(target - closestValue):
                closestValue = root.val
            root = root.left if root.val > target else root.right
        return(closestValue)
            