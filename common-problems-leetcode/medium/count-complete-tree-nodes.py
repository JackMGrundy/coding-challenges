"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
"""

# 100ms. 45th percentile.
# Simple bfs. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = collections.deque([root])
        numNodes = 0
        
        while q:
            cur = q.popleft()
            numNodes += 1
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        
        return numNodes



# 84 ms. 84th percentile.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def treeDepth(self, root):
        if not root:
            return 0
        return 1 + self.treeDepth(root.left)
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftTreeDepth = self.treeDepth(root.left)
        rightTreeDepth = self.treeDepth(root.right)
        
        if leftTreeDepth == rightTreeDepth:
            return 2**leftTreeDepth + self.countNodes(root.right)
        else:
            return 2**rightTreeDepth + self.countNodes(root.left)

"""
Notes:
A simple bfs/dfs/whatever gets you a quick answer if you count up all the nodes. That isn't necessary
though. We know the tree is full except the last row. We just need to node where that last node in the last row is.

My favorite way to think about this:

Then,
At each level, get the height of the tree (go as far left as you can). Then check the maxDepth of the
right subtree (go right and then left as long as you can.) 

If that value is 1 less than the maxdepth of
the root, then that means the left and right sub trees are both completely full. That means the last node
in the last row must in the right subtree. So add the 2^h-1 nodes of the left subtree plus 1 for the
root to the node count. Then recurse on the right subtree.

If the max depth of the right subtree is more than 1 less than that of the root, that means the left subtree has 
a different max depth than the right subtree. We just checked the farthest left node in the last 
row of the right subtree...and its depth was less than that of the left subtree...therefore the
last node in the last row must be in the left subtree. So add the 2^(h-1)-1 nodes of the right subtree
along with the root to the count of total nodes. Then recurse on the left subtree. 

"""