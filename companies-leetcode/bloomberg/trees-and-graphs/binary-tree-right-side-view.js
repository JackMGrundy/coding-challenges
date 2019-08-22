/*
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
*/


// 52ms. 92nd percentile.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
  if (root === null) {
      return [];
  }
  let res = [];
  let curLevel = 0;
  let level = 1;
  let stack = [ [root, level] ];
  while (stack.length > 0) {
      let curData = stack.shift();
      let curNode = curData[0];
      let level = curData[1];
      if (level > curLevel) {
          curLevel = level;
          res.push(curNode.val);
      }
      
      if (curNode.right !== null) {
          stack.push( [curNode.right, level+1] );
      }
      if (curNode.left !== null) {
          stack.push( [curNode.left, level+1] );
      }
  }
  
  return res;
};