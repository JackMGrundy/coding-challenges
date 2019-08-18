/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
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
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k < 2 || head == null) {
            return head;
        }
        
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode nodeBeforeGroup = dummy;
        int i = 0;
        
        while (head != null) {
            i++;
            if (i % k == 0) {
                nodeBeforeGroup = reverse(nodeBeforeGroup, head.next);
                head = nodeBeforeGroup.next;
            } else {
                head = head.next;
            }
        }
        return dummy.next;
    }
    
    private ListNode reverse(ListNode nodeBeforeGroup, ListNode nodeAfterGroup) {
        ListNode previous = nodeBeforeGroup;
        ListNode current = nodeBeforeGroup.next;
        ListNode next;
        ListNode newEndOfGroup = current;
        while (current != nodeAfterGroup) {
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        
        nodeBeforeGroup.next = previous;
        newEndOfGroup.next = nodeAfterGroup;
        return newEndOfGroup;
    }
}