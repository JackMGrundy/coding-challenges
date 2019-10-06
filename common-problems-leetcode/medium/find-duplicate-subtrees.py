"""
Given  a  binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any one of them.             

Two trees are duplicate if they have the same structure with same node values.  

Example 1:                                                                      

        1                                                                       

       / \                                                                      

      2   3                                                                     

     /   / \                                                                    

    4   2   4                                                                   

       /                                                                        

      4                                                                         

The following are two duplicate subtrees:                                       

      2                                                                         

     /                                                                          

    4                                                                           

and                                                                             

    4                                                                           

Therefore, you need to return above trees' root in the form of a list.          

"""
# 60ms. 98 percentile.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        treeCounts = collections.defaultdict(int)
        res = []
        
        def dfs(root):
            if not root:
                return "n"

            fullTree = str(root.val) + dfs(root.left) + dfs(root.right)
            if treeCounts[fullTree] == 1:
                res.append(root)
            treeCounts[fullTree] += 1

            return fullTree
        
        dfs(root)
        return res

"""
Notes:

Bottom leaf forms "n" + root.val + "n"...recursively build up representations of subtrees...
keep track of how many times each representation has been seen...only on the second time
add the root to a list to return.
"""