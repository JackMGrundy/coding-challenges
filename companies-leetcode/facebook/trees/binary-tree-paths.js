/*
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
*/


// 1st attempt: Iterative. 53 percentile.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    if (!root) return [];
    const res = [];
    let stack = [];
    var cur;
    root.val = "" + root.val
    stack.push(root)
    
    while (stack.length) {
        cur = stack.pop()
        
        if (!cur.left && !cur.right) {
            res.push(cur.val)
            continue;
        }
        if (cur.left) {
            cur.left.val = (cur.val + "->" + cur.left.val)
            stack.push( cur.left )            
        }
        if (cur.right) {
            cur.right.val = (cur.val + "->" + cur.right.val)
            stack.push( cur.right )            
        }
    }
    
    return(res);    
};

// 2nd attempt: recursive. 53 percentile
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    if (!root) return [];
    const res = [];
    
    function helper(cur) {
        if (!cur.left && !cur.right) {
            res.push(cur.val);
        }
        if (cur.left) {
            cur.left.val = (cur.val + "->" + cur.left.val);
            helper(cur.left);
        }
        if (cur.right) {
            cur.right.val = (cur.val + "->" + cur.right.val);
            helper(cur.right);
        }
    }
    root.val = "" + root.val;
    helper(root);
    return(res);  
};


// 3rd attemp: recursive. 99th percentile.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    if (!root) return [];
    const res = [];
    
    function helper(cur, str) {
        if (!cur.left && !cur.right) {
            res.push(str);
        }
        if (cur.left) {
            helper(cur.left, str + "->" + cur.left.val);
        }
        if (cur.right) {
            helper(cur.right, str + "->" + cur.right.val);
        }
    }
    helper(root, "" + root.val);
    return(res);  
};