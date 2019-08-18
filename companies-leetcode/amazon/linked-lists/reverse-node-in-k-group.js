/*
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
*/

// 75ms. 70th percentile
// Uses k memory...not sure if that's ok...
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
        let res = new ListNode(-1);
        let builder = res;
        
        while (head !== null) {
            let currentKGroup = [];
            
            for (let i = 0; i < k; i++) {
                currentKGroup.push(head.val);
                head = head.next;

                if (head === null && i < k-1) {
                    
                    for (let val of currentKGroup) {
                        builder.next = new ListNode(val);
                        builder = builder.next;
                    }
                    return res.next;
                } 
            }
            
            currentKGroup.reverse();
            for (let val of currentKGroup) {
                builder.next = new ListNode(val);
                builder = builder.next;
            }
        }
        
        return res.next;
    }
        
// attempt 2: 
/*
The above answer isn't valid. We aren't supposed to make new nodes. Above I was thinking of reversing as "switch the first
and the last nodes. Then the second and second to last...and so on". The key to this is to think of it simply as "makes each
node point to the one before it". Do that k times. Then attach that subchain to the result of reversing the next subchain
and so on. 

Just tricky handling all the pointers.
*/
// 72ms. 82nd percentile
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    if (k < 2 || head === null) {
        return head;
    }

    let reverseKGroup = function(nodeBeforeGroup, nodeAfterGroup) {
        let previous = nodeBeforeGroup;
        let current = nodeBeforeGroup.next;
        let next;
        let newEndOfGroup = current;
        while (current !== nodeAfterGroup) {
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        
        nodeBeforeGroup.next = previous;
        newEndOfGroup.next = nodeAfterGroup;
        return newEndOfGroup;
    }
    
    let dummy = new ListNode(-1);
    dummy.next = head;
    let nodeBeforeGroup = dummy;
    let i = 0;
    while (head !== null) {
        i += 1;
        
        if (i % k === 0) {
            nodeBeforeGroup = reverseKGroup(nodeBeforeGroup, head.next);
            head = nodeBeforeGroup.next;
        } else {
            head = head.next
        }
    }
    
    return dummy.next;
};