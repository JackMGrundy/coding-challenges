/*
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
*/

// 1ms. 99th percentile.
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) {
            return true;
        }
        int listLen = 0;
        ListNode runner = head;
        while (runner != null) {
            runner = runner.next;
            listLen++;
        }
        
        ListNode previous = head;
        ListNode current = previous.next;
        ListNode nextNode = current != null ? current.next : null;
        for (int i = 0; i < listLen/2 - 1; i++) {
            current.next = previous;
            previous = current;
            current = nextNode;
            nextNode = nextNode.next;
        }
        ListNode firstHalfHead = previous;
        ListNode secondHalfHead = listLen % 2 == 0 ? current : nextNode;
        
        while (firstHalfHead != null && secondHalfHead != null) {
            if (firstHalfHead.val != secondHalfHead.val) {
                return false;
            }
            firstHalfHead = firstHalfHead.next;
            secondHalfHead = secondHalfHead.next;
        }
        
        return true;
    }
}