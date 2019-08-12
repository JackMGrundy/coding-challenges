/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
*/

// 1st attempt: 71st percentile. 64 ms.
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
var isValidBST = function(root) {
    
    let helper = function(root, largestLeftAncestor, smallestRightAncestor) {
        if (root === null) {
            return true;
        }
        
        if (root.left !== null && !(largestLeftAncestor < root.left.val && root.left.val < root.val) ) {
            return false;
        }
        
        if (root.right !== null && !(root.val < root.right.val && root.right.val < smallestRightAncestor)) {
            return false;
        }
        
        return helper(root.left, largestLeftAncestor, root.val) && helper(root.right, root.val, smallestRightAncestor);
    }
    
    return helper(root, -Infinity, Infinity);
};