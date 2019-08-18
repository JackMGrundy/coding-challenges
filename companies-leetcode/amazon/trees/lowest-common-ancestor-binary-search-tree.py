"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""
# 1st attempt. 73rd percentile. 88ms. 
# Go to body of the tree...and then work up. post order traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowestAncestor = None
        
        def helper(root, p, q):
            nonlocal lowestAncestor
            
            if not root:
                return False
            
            leftHasSeenTarget = helper(root.left, p, q)
            rightHasSeenTarget = helper(root.right, p, q)
            rootIsTarget = (root == p) or (root == q)
            totalTargetsSeen = leftHasSeenTarget + rightHasSeenTarget + rootIsTarget
            
            if totalTargetsSeen == 2:
                lowestAncestor = root
            
            return leftHasSeenTarget or rightHasSeenTarget or rootIsTarget
            
        
        
        helper(root, p, q)
        return lowestAncestor



# 80ms 88th percentile
"""
Not as intuitive imo, but I like this approach. Easy to see that this works if left and right
are in different subtrees (i.e. the lowest common ancestor isn't p or q). However, say the lowest
ancestor is p or q, this will return as soon as it hits the first one. We'll never even see the
second one. That's ok though, because after we finish all the other calls and don't find anything,
we'll know that the second one must be below the first one we found. 

Nice way to save some calls
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        
        if left and right:
            return root
    
        return left or right
            