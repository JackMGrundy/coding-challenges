/*
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
*/
// 0ms. 100th percentile.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode nodeBeforeTargetSection = dummy;
        for (int i = 1; i < m; i++) {
            nodeBeforeTargetSection = nodeBeforeTargetSection.next;
        }
        
        ListNode newEndOfTargetSection = nodeBeforeTargetSection.next;
        ListNode previous = nodeBeforeTargetSection.next;
        ListNode current = previous.next;
        ListNode next;
        
        for (int i = 0; i < n-m; i++) {
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        
        nodeBeforeTargetSection.next = previous;
        newEndOfTargetSection.next = current;
        
        return dummy.next;
    }
}