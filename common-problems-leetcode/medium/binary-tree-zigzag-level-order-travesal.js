/*

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
*/

// 1st attempt: 95th percentile in speed
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    let res = [];
    if (!root) return res;
    
    let rev = false;
    let depth = 1;
    let level = [];
    let q = [ {node: root, d: 1} ] ;
    
    while (q.length) {
        let {node, d} = q.shift();
        if (d > depth) {
            if (rev) level.reverse()
            res.push(level);
            level = [];
            depth++;
            rev = !rev;
        }
        
        if (node) {
            level.push(node.val);
            if (node.left) q.push( {node: node.left, d: d+1} );
            if (node.right) q.push({node: node.right, d: d+1} );
        }
    }
    if (rev) level.reverse()
    res.push(level)
    
    return res;
};
