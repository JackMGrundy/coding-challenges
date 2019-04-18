/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
*/
// 1st attempt: 99th percentile in speed
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    var res = true;
    
    var helper = function(root, d) {
        if (!root) return d;
        
        let lD = helper(root.left, d+1);
        let rD = helper(root.right, d+1);
        
        if ( Math.abs( lD - rD ) > 1 ) {
            res = false;
        }
        
        return Math.max(lD, rD);
    }
    helper(root, 1);
    return res;
};