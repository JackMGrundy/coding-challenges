/*
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
*/


// 44ms. 98th percentile.
// Recursive
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if (head === null || head.next === null) {
        return head;
    }
    let headOldNext = head.next;
    head.next = headOldNext.next;
    headOldNext.next = head;
    headOldNext.next.next = swapPairs(head.next);
    return headOldNext;
};



// 48ms. 93rd percentile.
// Iterative...could have picked better var names...so tired, not going to worry about it rn. 
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    if (head === null || head.next === null) {
        return head;
    }
    let dummy = new ListNode(-1);
    let nodeBeforeSwapSection = dummy;
    
    while (head !== null && head.next !== null) {
        let oldHeadNext = head.next;
        nodeBeforeSwapSection.next = oldHeadNext;
        head.next = oldHeadNext.next;
        oldHeadNext.next = head;
        nodeBeforeSwapSection = head;
        head = head.next;
    }
    
    return dummy.next;
};