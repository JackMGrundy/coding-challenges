/*
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
 

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].
 

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.

*/
// 292ms. 86th percentile
var FreqStack = function() {
    this.countToStack = {};
    this.elementToCount = {};
    this.maxCount = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
FreqStack.prototype.push = function(x) {
    this.elementToCount[x] = x in this.elementToCount ? this.elementToCount[x]+1 : 1;
    this.maxCount = Math.max(this.maxCount, this.elementToCount[x]);
    if ( !(this.elementToCount[x] in this.countToStack) ) {
        this.countToStack[this.elementToCount[x]] = [x];
    } else {
        this.countToStack[this.elementToCount[x]].push(x);
    }
};

/**
 * @return {number}
 */
FreqStack.prototype.pop = function() {
    let maxStack = this.countToStack[this.maxCount];
    let res = maxStack.pop();
    this.elementToCount[res] -= 1;
    if (maxStack.length === 0) {
        delete this.countToStack[this.maxCount];
        this.maxCount -= 1;
    }
    return res;
};

/** 
 * Your FreqStack object will be instantiated and called as such:
 * var obj = new FreqStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 */

