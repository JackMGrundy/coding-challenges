/*

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/

// 84ms. 74th percentile.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if (head === null || head.next === null) {
        return head;
    }
    
    let prev = head;
    let slow = head;
    let fast = head;
    let res = head;
    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    
    prev.next = null;
    prev = slow
    current = slow.next
    after = null;
    slow.next = null;
    
    while (current !== null) {
        after = current.next;
        current.next = prev;
        prev = current;
        current = after;
    }
    
    firstHalfHead = head;
    secondHalfHead = prev;
    
    while (firstHalfHead !== null && secondHalfHead !== null) {
        let temp = firstHalfHead.next;
        firstHalfHead.next = secondHalfHead;
        firstHalfHead = temp;
        
        if (firstHalfHead !== null) {
            let temp = secondHalfHead.next;
            secondHalfHead.next = firstHalfHead;
            secondHalfHead = temp;
        }
    }
        
    return res;
};