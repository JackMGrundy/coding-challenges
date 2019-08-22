/*
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example:



Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
*/


/*
Intuition: Put a cap on the current level. Keep pointers to the current parent and the last child seen.
Move the parent along until you see a parent with a child. Then link the last child seen to the new child.
Move the child pointer forwards.

To start a new level, set parent to next of the cap of the level just completed. 
*/

// 0ms. 100th percentile.
/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val,Node _left,Node _right,Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
  public Node connect(Node root) {
      Node res = root;
      
      while (root != null) {
          Node levelStart = new Node(-1);
          Node currentChild = levelStart;
          while (root != null) {
              if (root.left != null) {
                  currentChild.next = root.left;
                  currentChild = currentChild.next;
              }
              if (root.right != null) {
                  currentChild.next = root.right;
                  currentChild = currentChild.next;
              }
              
              root = root.next;
          }
          
          root = levelStart.next;            
      }
      
      return res;
  }
}