/*
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
*/
// 92nd percentile. 48ms.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
    let dummy = new ListNode(-1);
    dummy.next = head;
    let nodeBeforeTargetSection = dummy;
    for (let i = 1; i < m; i++) {
        nodeBeforeTargetSection = nodeBeforeTargetSection.next;
    }
    
    let previous = nodeBeforeTargetSection.next;
    let newEndOfTargetSection = nodeBeforeTargetSection.next;
    let current = previous.next;
    let next;
    for (let i = 0; i < n-m; i++) {
        next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    
    nodeBeforeTargetSection.next = previous;
    newEndOfTargetSection.next = current;
    
    return dummy.next;
};