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
// 97th percentile. 2ms.
// Gosh those indices are hairy. 
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
  public TreeNode buildTree(int[] preorder, int[] inorder) {
      
      Map<Integer, Integer> inorderPositions = new HashMap<Integer, Integer>();
      for (int i = 0; i < inorder.length; i++) {
          inorderPositions.put(inorder[i], i);
      }
      
      return helper(preorder, 0, preorder.length, inorder, 0, inorder.length, inorderPositions);
  }
  
  TreeNode helper(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd, Map<Integer, Integer> inorderPositions) {
      if (inEnd > inStart) {
          int rootValue = preorder[preStart];
          int rootInorderIndex = inorderPositions.get(rootValue);
          TreeNode root = new TreeNode(rootValue);
          int leftValsLeft = rootInorderIndex - inStart;
          int rightValsLeft = inStart-rootInorderIndex;
          
          root.left = helper(preorder, preStart+1, preStart+leftValsLeft, inorder, inStart, rootInorderIndex, inorderPositions);
          root.right = helper(preorder, preStart+leftValsLeft+1, preStart+leftValsLeft+1+rightValsLeft, inorder, rootInorderIndex+1, inEnd, inorderPositions);
          return root;
      } else {
          return null;
      }
  }
}