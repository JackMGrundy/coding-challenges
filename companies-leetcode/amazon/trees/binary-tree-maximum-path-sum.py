"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# 3rd attempt. 98th percentile. 88ms.
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        bestPathValue = -float("inf")
        
        def helper(root):
            nonlocal bestPathValue
            
            if not root:
                return 0
            
            leftsBestBranch = helper(root.left)
            rightsBestBranch = helper(root.right)
            rootsBestBranch = max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch)
                                         
            bestPathValue =   max(bestPathValue,             \
                                  rootsBestBranch,            \
                                  root.val + leftsBestBranch + rightsBestBranch)
            
            return rootsBestBranch
        
        helper(root)
        return bestPathValue


"""
Notes:

Great question. Very intuitive actually.

Any solution we pick is only allowed to branch in two different directions at most once. Therefore at each node we record the "rootsBestBranch" meaning that if
we use this root in a path, what is the best value you can get out of it? We return that from each level to the level above it.

And to actually find the answer, we simply check at each node what's the best value we can get out of making the node the root. Given that we know the best
we can get out of the left and right branches, this is easy. Its either the just the roots value, the roots value + one of the branches, or the roots value
+ both branches best values. 
"""