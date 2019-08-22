/*
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
*/

// 0ms. 100th percentile.
/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node() {}

    public Node(int _val,Node _prev,Node _next,Node _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/
class Solution {
    public Node flatten(Node head) {
        if (head == null) {
            return null;
        }
        
        Node cur = head;
        Node res = cur;
        Stack<Node> stack = new Stack<Node>();
        while (cur != null) {
            
            while (cur.child == null && cur.next != null) {
                cur = cur.next;
            }
            
            while (cur.child != null) {
                if (cur.next != null) {
                    stack.push(cur.next);
                }
                cur.next = cur.child;
                cur.child.prev = cur;
                cur.child = null;
                cur = cur.next;
            }
            
            while (cur.next == null) {
                if (stack.isEmpty()) {
                    return res;
                }
                
                cur.next = stack.pop();
                cur.next.prev = cur;
                cur.child = null;
                cur = cur.next;
            }
        }
        return res;
    }
}