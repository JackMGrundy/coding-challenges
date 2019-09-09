"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

# 1st attempt: 100th percentile. Iterative. Standard pre order dfs.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: 
            return None
        stack = [root]
        prev = TreeNode(-1)
        
        while stack:
            cur = stack.pop()
            
            for c in [cur.right, cur.left]:
                if c:
                    stack.append(c)
            
            prev.right = cur
            prev.left = None
            prev = prev.right


"""
Notes:

Iteative pre order dfs...
Process the current node. Put the children on the stack in the opposite order that you want to process.
Say you put left on last. Then you'll always be popping off a left node until you've gon all the way down to the
right. Then will go back to the right nodes when we're out of left.

As for this specific problem...At each step we want the last node that was processed. So we just
keep track of a previous. 
"""