/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
*/

// post order traversal: 84th percentile. 64ms.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    let lowestAncestor = null;
    
    
    let helper = function(root, p, q) {
        
        if (root === null) {
            return false;
        }
        
        let leftHasSeenTarget = helper(root.left, p, q);
        let rightHasSeenTarget = helper(root.right, p, q);
        let rootIsTarget = (root === p) || (root === q);
        let numTargetsSeen = leftHasSeenTarget + rightHasSeenTarget + rootIsTarget;
        
        if (numTargetsSeen === 0) {
            return false;
        }
        
        else if (numTargetsSeen === 1) {
            return true;
        }
        
        else if (numTargetsSeen === 2) {
            lowestAncestor = root;
            return false;
        }
    }
    
    helper(root, p, q);
    return lowestAncestor;
    
};




// In order traversal: 64ms. 84th percentile
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    
    if (root === p || root === q || root === null) {
        return root;
    }
    
    let left = lowestCommonAncestor(root.left, p, q);
    let right = lowestCommonAncestor(root.right, p, q);
    
    if (left !== null && right !== null) {
        return root;
    }
    
    return left === null ? right : left;
};