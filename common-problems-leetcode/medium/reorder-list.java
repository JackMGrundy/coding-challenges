/*

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/
// 1ms. 100th percentile.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        
        ListNode prev = head;
        ListNode slow = head;
        ListNode fast = head;
        ListNode res = head;
        
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null;
        prev = slow;
        ListNode current = slow.next;
        slow.next = null;
        ListNode after = null;
        
        while (current != null) {
            after = current.next;
            current.next = prev;
            prev = current;
            current = after;
        }
        
        ListNode firstHalfHead = head;
        ListNode secondHalfHead = prev;
        ListNode temp = null;
        
        while (firstHalfHead != null && secondHalfHead != null) {
            temp = firstHalfHead.next;
            firstHalfHead.next = secondHalfHead;
            firstHalfHead = temp;
            
            if (firstHalfHead != null) {
                temp = secondHalfHead.next;
                secondHalfHead.next = firstHalfHead;
                secondHalfHead = temp;
            }
        }
        
        return;
    }
}