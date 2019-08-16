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


// 87th percentile. 68ms.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
   let bestPathValue = -Infinity
   
   let helper = function(root) {
       
       if (root.left === null && root.right === null) {
           bestPathValue = Math.max(bestPathValue, root.val);
           return root.val;
       }
       
       let leftsBestBranch = root.left !== null ? helper(root.left) : -Infinity;
       let rightsBestBranch = root.right !== null ? helper(root.right) : -Infinity;
       let rootsBestBranch = Math.max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch);
       
       bestPathValue = Math.max(bestPathValue,
                                rootsBestBranch,
                                root.val + leftsBestBranch + rightsBestBranch);
       
       return rootsBestBranch;
   }
   
   helper(root);
   return bestPathValue;
};



// 72ms. 73rd percentile.
// cleaner
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function(root) {
   let bestPathValue = -Infinity
   
   let helper = function(root) {
       if (root === null) {
           return 0
       }
           
       let leftsBestBranch = helper(root.left);
       let rightsBestBranch = helper(root.right)
       let rootsBestBranch = Math.max(root.val, root.val + leftsBestBranch, root.val + rightsBestBranch);
       
       bestPathValue = Math.max(bestPathValue,
                                rootsBestBranch,
                                root.val + leftsBestBranch + rightsBestBranch);
       
       return rootsBestBranch;
   }
   
   helper(root);
   return bestPathValue;
};