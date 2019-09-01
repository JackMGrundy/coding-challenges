/*
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
Accepted
201,935
Submissions
547,333
*/

// 80ms. 97th percentile.
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

let merge = function(l1, l2) {
    
    let head = new ListNode(-1);
    let temp = head;
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            temp.next = l1;
            l1 = l1.next;
        } else {
            temp.next = l2; 
            l2 = l2.next;
        }
        temp = temp.next;
    }
    
    if (l1 !== null) {
        temp.next = l1;
    } else {
        temp.next = l2;
    }
    
    return head.next;
}

var sortList = function(head) {
    if (head === null || head.next === null) {
        return head;
    }
    
    let fast = head;
    let slow = head;
    let prev = head;
    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    
    prev.next = null;
    
    let l1 = sortList(head);
    let l2 = sortList(slow);
    return merge(l1, l2);
};



/*
Notes:
This is O(log(N)) space. To get it to constant space, you'd have to do iterative/bottom up
merge sort. 

Note the prev.next = null line to break apart the two component lists...
*/