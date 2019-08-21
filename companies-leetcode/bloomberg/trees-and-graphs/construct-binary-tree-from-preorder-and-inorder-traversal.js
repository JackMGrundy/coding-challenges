/*
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
*/
// 80ms. 69th percentile.
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    
  let helper = function(preorder, leftInorder, rightInorder) {
      if (rightInorder > leftInorder) {
          let rootVal = preorder.shift();
          let rootInorderIndex = inorder.indexOf(rootVal);
          let root = new TreeNode(rootVal);
          root.left = helper(preorder, leftInorder, rootInorderIndex);
          root.right = helper(preorder, rootInorderIndex+1, rightInorder);
          return root;
      } else {
          return null;
      }
  }
  
  return helper(preorder, 0, inorder.length);
};