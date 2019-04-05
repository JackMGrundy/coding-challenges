/*
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 */
// 1st attempt: 97th percentile in speed
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    if (nums.length===0) return null;
    
    let mid = Math.floor(nums.length / 2);
    let root = new TreeNode(nums[mid]);
    if (nums.length===1) return root;
    
    let left = sortedArrayToBST(nums.slice(0, mid));
    if (left) root.left = left;
    
    let right = sortedArrayToBST(nums.slice(mid+1, nums.length));
    if (right) root.right = right;
    
    return root;
};