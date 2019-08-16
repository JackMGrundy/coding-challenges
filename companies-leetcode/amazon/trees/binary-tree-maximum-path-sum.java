/*
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
*/

// 1ms. 99th percentile.
// this isn't great though...didn't deal with overflow...cheated a bit with the negative constants
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
   int bestPathValue = -10000;
   
   public int maxPathSum(TreeNode root) {
       helper(root);
       return bestPathValue;
   }
   
   public int helper(TreeNode root) {
       
       if (root.left == null && root.right == null) {
           bestPathValue = Math.max(bestPathValue, root.val);
           return root.val;
       }
       
       int leftsBestBranch = root.left != null ? helper(root.left) : -10000;
       int rightsBestBranch = root.right != null ? helper(root.right) : -10000;
       int rootsBestBranch = Math.max(root.val, Math.max(root.val + leftsBestBranch, root.val + rightsBestBranch));
       
       bestPathValue = Math.max(bestPathValue,
                                Math.max(rootsBestBranch,
                                         root.val + leftsBestBranch + rightsBestBranch
                                         ));
       return rootsBestBranch;
   }
}





// 1ms. 99th percentile. Deals with contants / overflow and its cleaner
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
   int bestPathValue = Integer.MIN_VALUE;
   
   public int maxPathSum(TreeNode root) {
       helper(root);
       return bestPathValue;
   }
   
   public int helper(TreeNode root) {
       
       if (root == null) {
           return 0;
       }
       
       int leftsBestBranch = helper(root.left);
       int rightsBestBranch = helper(root.right);
       int rootsBestBranch = Math.max(root.val, Math.max(root.val + leftsBestBranch, root.val + rightsBestBranch));
       
       bestPathValue = Math.max(bestPathValue,
                                Math.max(rootsBestBranch,
                                         root.val + leftsBestBranch + rightsBestBranch
                                         ));
       return rootsBestBranch;
   }
}