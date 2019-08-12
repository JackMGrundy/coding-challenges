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
// 1st attempt: 24th percentile 2ms.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Stack;
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }
        Stack<TreeNode> s = new Stack<TreeNode>();
        TreeNode previous = null;
        while (s.size() > 0 || root != null) {
            if (root != null) {
                s.push(root);
                root = root.left;
            } else {
                TreeNode current = s.pop();
                if (previous != null && current.val <= previous.val) {
                    return false;
                }
                previous = current;
                root = previous.right;
            }
        }
        
        return true;
    }
}


// 2nd attempt. 0ms. 100th percentile
// recursive
// Note I did the double if's because I found it easier to read
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Stack;
class Solution {
    public boolean isValidBST(TreeNode root) {
        return helper(root, null, null);
    }
    
    private boolean helper(TreeNode root, TreeNode largestLeftAncestor, TreeNode smallestRightAncestor) {
        if (root == null) {
            return true;
        }
        
        if (root.left != null) {
            if ( (largestLeftAncestor != null && largestLeftAncestor.val >= root.left.val) || root.left.val >= root.val) {
                return false;
            } 
        }

        if (root.right != null) {
            if ( (smallestRightAncestor != null && smallestRightAncestor.val <= root.right.val) || root.right.val <= root.val) {
                return false;
            } 
        }
        
        return helper(root.left, largestLeftAncestor, root) && helper(root.right, root, smallestRightAncestor);
    }
}