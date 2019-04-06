/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
*/

// 1st attempt 
/*
Doesn't work...but already spent too much time on this...key takeaway: javascript can't use objects as keys
in dictionaries (other objects). It just stringifies them all to the same thing. Javascript also doesn't seem to have
a great internal mechanism for hashing...I started to make a not so great but probably good enough to pass the tests
stringify function...but moving on...
*/
/**
 * // Definition for a Node.
 * function Node(val,next,random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */
/**
 * @param {Node} head
 * @return {Node}
 */
var id = function(node) {
    res = "id";
    if (node === undefined || node === null) {
        return res;
    }
    if (node.val) res += node.val;
    if (node.next) res += node.next.val;
    if (node.random) res += node.random.val;
    res = res.replace(/\-/g, "")
    // console.log(res)
    return res;
}

var copyRandomList = function(head) {
if (!head) return null
let memo = {};
let origRunner = head;
let res = new Node(head.val, null, null);
let newRunner = res;
memo[head] = res;
var cpy;
while (origRunner) {
    if (origRunner.next) {
        cpy = new Node(origRunner.next.val, null, null);
        // console.log(Object.getOwnPropertyNames(origRunner))
        memo[id(origRunner.next)] = cpy;
        newRunner.next = cpy;
    }
    origRunner = origRunner.next;
    newRunner = newRunner.next;
}

origRunner = head;
newRunner = res;

while (origRunner) {
    if (origRunner.random) {
        // console.log(origRunner.random.val)
        newRunner.random = memo[origRunner.random];
    }
    origRunner = origRunner.next;
    newRunner = newRunner.next;
}

return res;
};