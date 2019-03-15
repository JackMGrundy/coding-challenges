/*
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
*/
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let slow = head,
        fast = head;
    let prev = new ListNode(-1);
    
    for (let i = 0; i < n; i++) {
        fast = fast.next;
    }
    
    if (!fast) return(head.next);
    
    while (fast) {
        prev = slow;
        slow = slow.next;
        fast = fast.next;
    }
    
    prev.next = slow.next;
    return(head);
};