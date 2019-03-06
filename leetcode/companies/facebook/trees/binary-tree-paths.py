"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Attemp 1: 50th percentile. Iterative.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None: return([])
        res = []
        stack = [(root, str(root.val))]
        
        while stack:
            cur, curPath = stack.pop()
            
            if cur.left==None and cur.right==None:
                res.append(curPath)
            
            for c in [cur.left, cur.right]:
                if c != None:
                    stack.append( (c, curPath + "->" + str(c.val)) )
        
        return(res)
                
# Attempt 2: recursive. 34th percentile in speed. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
                    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None: return([])
        res = []
        
        def helper(node: TreeNode) -> List[str]:
            if node.left==None and node.right==None:
                res.append(node.val)
            else:  
                for c in [node.left, node.right]:
                    if c:
                        c.val = node.val + "->" + str(c.val)
                        helper(c)
                    
        root.val = str(root.val)
        helper(root)
        return(res)
    

# Attempt 3: recursive. 46th percentile in speed. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
                    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None: return([])
        res = []
        
        def helper(node: TreeNode) -> List[str]:
            if node.left==None and node.right==None:
                res.append(node.val)
            for c in [node.left, node.right]:
                if c:
                    c.val = node.val + "->" + str(c.val)
                    helper(c)
                    
        root.val = str(root.val)
        helper(root)
        return(res)

# Attempt #4: 97th percentile (not that much faster actually...a lot of ppl in this group)
# Intuition. My first recursive attempts were essentially preorder traversals
# that pass the path information down. That means that each bottom node (of which
# there could be many more than top nodes) are being handed an almost complete (long)
# path. In this attempt, it is a postorder traversal, so the numberous leaf nodes
# process a single number, the layer above them 2, and so on. Therefore, the total amount 
# of info being passed is lessened...the fewer nodes closer to the root handle longer
# paths, while the many nodes closer to the leaves handle shorter paths.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
                    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None: return([])
        return(helper(root))
    
def helper(node):
    res = []
    
    if node.left:
        for i in helper(node.left):
            res.append(str(node.val) + "->" + i)
    
    if node.right:
        for i in helper(node.right):
            res.append(str(node.val) + "->" + i)
    
    if not node.left and not node.right:
        res.append(str(node.val))
    
    return(res)