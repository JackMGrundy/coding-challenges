/*
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
*/

// 68ms. 94 percentile.
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

let treeDepth = function(root) {
    if (root === null) {
        return 0;
    } else {
        return 1 + treeDepth(root.left);
    }
}

var countNodes = function(root) {
    if (root === null) {
        return 0;
    }
    let leftTreeDepth = treeDepth(root.left);
    let rightTreeDepth = treeDepth(root.right);
    if (leftTreeDepth !== rightTreeDepth) {
        return Math.pow(2, rightTreeDepth) + countNodes(root.left);
    }
    else {
        return Math.pow(2, leftTreeDepth) + countNodes(root.right);
    }
};