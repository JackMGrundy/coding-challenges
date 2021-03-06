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

// 0ms. 100th percentile.
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
    
    int treeDepth(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            return 1 + treeDepth(root.left);
        }
    }
    
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftTreeDepth = treeDepth(root.left);
        int rightTreeDepth = treeDepth(root.right);
        if (leftTreeDepth == rightTreeDepth) {
            return (int) Math.pow(2, leftTreeDepth) + countNodes(root.right);
        } else {
            return (int) Math.pow(2, rightTreeDepth) + countNodes(root.left);
        }
    }
}