"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.
"""
# 1st attempt: 74th percentile in speed. Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1
        
        s1 = [ t1 ]
        s2 = [ t2 ]
        res = TreeNode(t1.val+t2.val)
        sM = [ res ]
        while sM:
            cur1 = s1.pop(); cur2 = s2.pop(); curM = sM.pop()
            
            # right
            if cur1.right and cur2.right:
                curM.right = TreeNode(cur1.right.val+cur2.right.val)
                s1.append(cur1.right); s2.append(cur2.right); sM.append(curM.right); 
            elif cur1.right:
                curM.right = cur1.right
            elif cur2.right:
                curM.right = cur2.right
            # left
            if cur1.left and cur2.left:
                curM.left = TreeNode(cur1.left.val+cur2.left.val)
                s1.append(cur1.left); s2.append(cur2.left); sM.append(curM.left); 
            elif cur1.left:
                curM.left = cur1.left
            elif cur2.left:
                curM.left = cur2.left
            
        return res


# 2nd attempt: still 74th percentile in speed. Recursive.
"""
I like this solution much more. In the first attempt, a whole new tree is made, but it akwardly draws from pieces
of the original two trees with shallow copies.

This solution merges the second tree into the first tree.

This simplifies things in part, because you don't have to worry about managing where the new pieces connect
to the final tree. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        elif not t2: return t1
        
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1

