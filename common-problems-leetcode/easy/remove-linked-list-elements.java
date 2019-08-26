/*
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
*/
// 1ms. 98th percentile. 


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode runner = dummy;
        
        while (runner != null) {
            while (runner.next != null) {
                if (runner.next.val == val) {
                    runner.next = runner.next.next;
                } else {
                    break;
                }
            }
            runner = runner.next;
        }
        return dummy.next;
    }
}