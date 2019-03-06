/*
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
*/

// Attempt 1: recursive. 78th percentile in speed. 
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
var diameterOfBinaryTree = function(root) {
    if (!root) return(0);
    var longestPath = 0;
    
    function helper(node) {
        let l = 0,
            r = 0;
        
        if (node.left) {
            l = helper(node.left) + 1;
        }
        if (node.right) {
            r = helper(node.right) + 1;
        }
        if (r+l > longestPath) {
            longestPath = r+l;
        }
        if (!node.left && !node.right) {
            return(0);
        } else {
            return(Math.max(l, r));
        }
    }
    
    helper(root);
    return(longestPath);
};