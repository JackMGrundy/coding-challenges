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
Doesn't work...key takeaway: javascript can't use objects as keys
in dictionaries (other objects). It just stringifies them all to the same thing. Javascript also doesn't seem to have
a great internal mechanism for hashing...I started to make a not so great but probably good enough to pass the tests
stringify function...
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


// 2nd attempt: 620ms. 93rd percentile
/*
All hail ES6 maps
https://medium.com/front-end-weekly/es6-map-vs-object-what-and-when-b80621932373

It's interesting that even the fastest solutions are only ~600 ms. That's more than 10 times slower than Python. 
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
var copyRandomList = function(head) {
    if (head === null) {
        return null;
    }
    
    let res = new Node(head.val, head.next, head.random);
    let normalLinker = res;
    const map = new Map();
    map.set(head, res);
    
    // Link normal nodes
    while (head.next !== null) {
        let newNode = new Node(head.next.val, head.next.next, head.next.random);
        normalLinker.next = newNode;
        map.set(head.next, newNode);
        
        head = head.next;
        normalLinker = normalLinker.next;
    }
    
    // Link random nodes
    let randomLinker = res;
    while (randomLinker !== null) {
        if ( randomLinker.random !== null) {
            randomLinker.random = map.get(randomLinker.random);
        }
        randomLinker = randomLinker.next
    }
    
    return res;
};

// 3rd attempt: recursive. 636 ms. 70th percentile. 
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

let copied = new Map();

var copyRandomList = function(head) {
    if (head === null) {
        return null;
    }
    if (copied.has(head)) {
        return copied.get(head);
    }
    else {
        let newNode = new Node(head.val, null, null);
        copied.set(head, newNode);
        newNode.next = copyRandomList(head.next);
        newNode.random = copyRandomList(head.random);
        
        return newNode;
    }  
};



// 4th attempt. recursive. 616ms. 96th percentile. 
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

let copied = new Map();

var copyRandomList = function(head) {
    if (head === null) return null;
    if (copied.has(head)) return copied.get(head);
    
    let newNode = new Node(head.val, null, null);
    copied.set(head, newNode);
    newNode.next = copyRandomList(head.next);
    newNode.random = copyRandomList(head.random);

    return newNode;
};