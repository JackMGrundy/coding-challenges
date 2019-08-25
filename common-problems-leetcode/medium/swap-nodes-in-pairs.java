/*
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
*/
// Recusrive.
// 0ms. 100h percentile.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode a) {
        if (a == null || a.next == null) {
            return a;
        }
        ListNode b = a.next;
        a.next = b.next;
        b.next = a;
        b.next.next = swapPairs(a.next);
        return b;
    }
}


// Iterative
// 0ms. 100th percentile
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode a) {
        if (a == null || a.next == null) {
            return a;
        }
        
        ListNode dummy = new ListNode(-1);
        ListNode nodeBeforeSwapSection = dummy;
        
        while (a != null && a.next != null) {
            ListNode b = a.next;
            nodeBeforeSwapSection.next = b;
            a.next = b.next;
            b.next = a;
            nodeBeforeSwapSection = a;
            a = a.next;
        }
        
        return dummy.next;
    }
}