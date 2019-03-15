/*

*/
// 1st attempt: 83rd percentile. Cleaner than faster implementations. Only 
// a few ms out of ~65 slower. Same time complexity.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function(root) {
    if (!root) return null;
    let stack = [],
        prev = new TreeNode(-1)
    stack.push(root);
    
    while (stack.length>0) {
        let cur = stack.pop();
        if (cur && cur.right) stack.push(cur.right);
        if (cur && cur.left) stack.push(cur.left);
        
        prev.right = cur;
        prev.left = null;
        prev = prev.right;
    }
};