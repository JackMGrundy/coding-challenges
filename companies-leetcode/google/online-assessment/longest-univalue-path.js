/*
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
*/
// 93rd percentile in speed
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
var longestUnivaluePath = function(root) {
    if (!root) return 0;
    var res = 0;
    
    var helper = function(root) {
        if (!root) return 0;
        
        let l = helper(root.left);
        let r = helper(root.right);
        
        root.left && root.left.val===root.val ? l += 1 : l = 0;
        root.right && root.right.val===root.val ? r += 1 : r = 0;
        
        res = Math.max(res, l+r);
        
        return(Math.max(l, r));
    }
    
    helper(root);
    return res;
    
};