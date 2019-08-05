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

// 1st attempt: 93rd percentile, 1ms
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.Queue;
import java.util.LinkedList;
import java.util.Collections;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) {
            return res;
        }
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        int order = 1;
        List<Integer> level = new ArrayList<Integer>();
        
        while (q.size() > 0) {
            level = new ArrayList<Integer>();
            int numElements = q.size();
            
            for (int i = 0; i < numElements; i++) {
                TreeNode node = q.remove();
                
                if (node.left != null) {
                    q.add(node.left);
                }
                if (node.right != null) {
                    q.add(node.right);
                }
                
                level.add(node.val);
            }
            if (order == -1) {
                Collections.reverse(level);
            }
            order *= -1;
            res.add(level);
        }
        
        return res;
    }
}