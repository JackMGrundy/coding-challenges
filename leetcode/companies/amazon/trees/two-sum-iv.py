"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
from collections import deque
class TreeNode:
    def __init__(self, num):
        self.val = num
        self.right = None
        self.left = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = deque()
        queue.append(root)
        matches = set()
        
        while queue:
            curNode = queue.popleft()
            if curNode.val in matches: return(True)
            matches.add(k-curNode.val)
            
            for c in [curNode.left, curNode.right]:
                if c: queue.append(c)
        return(False)


if __name__=='__main__':
    print("a")