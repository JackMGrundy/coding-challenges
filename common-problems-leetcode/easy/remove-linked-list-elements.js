/*
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
*/

// 68ms. 89th percentile.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    let dummy = new ListNode(-1);
    dummy.next = head;
    let runner = dummy;
    while (runner !== null) {
        while (runner.next != null) {
            if (runner.next.val === val) {
                runner.next = runner.next.next;
            } else {
                break;
            }
        }
        
        runner = runner.next;
    }
    
    
    
    return dummy.next;
};