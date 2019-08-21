/*
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
*/
// 102ms. 92nd percentile.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let stack1 = [];
    let stack2 = [];
    
    while (l1 !== null) {
        stack1.push(l1.val);
        l1 = l1.next;
    }
    while (l2 !== null) {
        stack2.push(l2.val);
        l2 = l2.next;
    }
    
    head = null;
    let carry = 0;
    while (stack1.length > 0 || stack2.length > 0 || carry === 1) {
        let nextVal = carry;
        if (stack1.length > 0) {
            nextVal += stack1.pop();
        }
        if (stack2.length > 0) {
            nextVal += stack2.pop();
        }
        carry = nextVal > 9 ? 1 : 0;
        nextVal = nextVal > 9 ? nextVal-10 : nextVal;
        let temp = new ListNode(nextVal);
        temp.next = head;
        head = temp;
    }
    
    return head;
};