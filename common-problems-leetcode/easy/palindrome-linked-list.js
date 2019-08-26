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

// 64ms. 66th percentile.
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    if (head === null || head.next === null) {
        return true;
    }
    
    let listLen = 0;
    let runner = head;
    while (runner !== null) { 
        runner = runner.next;
        listLen++;
    }
    let previous = head;
    let current = previous.next;
    let nextNode = current !== null ? current.next : null;
    for (let i = 0; i < Math.floor(listLen/2)-1; i++) {
        current.next = previous;
        previous = current;
        current = nextNode;
        nextNode = current.next;
    }
    let firstHalfHead = previous;
    let secondHalfHead = listLen % 2 === 1 ? nextNode : current;
    
    while (firstHalfHead !== null && secondHalfHead != null) {
        if (firstHalfHead.val !== secondHalfHead.val) {
            return false;
        }
        firstHalfHead = firstHalfHead.next;
        secondHalfHead = secondHalfHead.next;
    }
    return true;
};