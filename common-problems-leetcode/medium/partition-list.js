/*
Given  a linked list and a value x, partition it such that all nodes less than x
come before nodes greater than or equal to x.                                   

You  should preserve the original relative order of the nodes in each of the two
partitions.                                                                     

Example:                                                                        

Input: head = 1->4->3->2->5->2, x = 3                                           

Output: 1->2->2->4->3->5                                                        

*/

// 44ms. 99.7 percentile.
// Could make this more readable by cutting the two inner while's...

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    let firstPart = new ListNode(-1);
    let secondPart = new ListNode(-1);
    let firstPartHead = firstPart;
    let secondPartHead = secondPart;
    
    while (head) {
        while (head && head.val < x) {
            firstPart.next = head;
            firstPart = firstPart.next;
            head = head.next
        }
        while (head && x <= head.val) {
            secondPart.next = head;
            secondPart = secondPart.next;
            head = head.next
        }
    }
    
    secondPart.next = null;
    firstPart.next = secondPartHead.next;
    return firstPartHead.next;
};


/*
One little thing to note is the need to unlike the end of "secondPart"
with the null line. Otherwise you'll get a circular reference.

*/