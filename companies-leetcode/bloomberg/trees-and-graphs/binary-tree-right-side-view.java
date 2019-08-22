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

// 1 ms. 99th percentile.
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
  public List<Integer> rightSideView(TreeNode root) {
      if (root == null) {
          return new ArrayList<Integer>();
      }
      
      int curLevel = 0;
      int level = 1;
      Queue<Pair> q = new LinkedList<Pair>();
      List<Integer> res = new ArrayList<Integer>();
      Pair rootPair = new Pair(root, level);
      q.add(rootPair);
      
      while (q.size() > 0) {
          Pair curPair = q.remove();
          TreeNode cur = curPair.node;
          level = curPair.level;
          
          if (level > curLevel) {
              curLevel = level;
              res.add(cur.val);
          }
          
          if (cur.right != null) {
              Pair temp = new Pair(cur.right, level+1);
              q.add(temp);
          }
          if (cur.left != null) {
              Pair temp = new Pair(cur.left, level+1);
              q.add(temp);
          }
      }

      return res;
  }
}


class Pair {
  public TreeNode node;
  public int level;
  
  public Pair(TreeNode node, int level) {
      this.node = node;
      this.level = level;
  }
  
}