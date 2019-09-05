"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# 148ms. 56th percentile.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder:
            rootVal = preorder.pop(0)
            rootInorderIndex = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder, inorder[0:rootInorderIndex])
            root.right = self.buildTree(preorder, inorder[rootInorderIndex+1:])
            return root


"""
Notes:
Preorder always lets you know the left of each node...however, it doesn't let you know where
rights are attached. 

Inorder lets you break the tree into two pieces.

The strategy:
The first node in preorder must be the root. Make a node for it. We find its location in inorder
to identify the two subtrees on the left and right. 

We make a recursive call on the remaining preorder and the left tree subsection from inorder. We know
that if root has a left, then the first element of preorder will be it. So in the recursive call
we pop off the next element of preorder and return it to attach it as a left.

However, the big thing to remember is that we first check if inorder exists. Why? while we know that
if root has a left it will be the next element of preorder, we don't know if it has a left. Inorder
tells us that - when we recurse, we pass the section of the inorder that corresponds with all the nodes
left of the root. If it's empty, there is no left. 

Say we recurse and there are no nodes in the left tree, then we know that the next element of preorder
is the right...and so we continue.
"""