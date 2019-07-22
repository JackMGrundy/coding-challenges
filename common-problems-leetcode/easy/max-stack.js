/*
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
Accepted
22,477
Submissions
56,256
*/

/*
Javascript doesn't have a built in heap, so I implemeneted one and started to create a solution with it.
This is silly though. Too much for an interview question. Going to solve it with built in methods.
*/
/**
 * initialize your data structure here.
 */
var MaxStack = function() {
    this.heap = new MaxHeap();
    this.stack = [];
    this.stackPoppedIds = new Set();
    this.heapPoppedIds = new Set();
    this.nextId = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
MaxStack.prototype.push = function(x) {
    this.heap.push([this.nextId, x]);
};

/**
 * @return {number}
 */
MaxStack.prototype.pop = function() {
    
};

/**
 * @return {number}
 */
MaxStack.prototype.top = function() {
    
};

/**
 * @return {number}
 */
MaxStack.prototype.peekMax = function() {
    
};

/**
 * @return {number}
 */
MaxStack.prototype.popMax = function() {
    
};

/** 
 * Your MaxStack object will be instantiated and called as such:
 * var obj = new MaxStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.peekMax()
 * var param_5 = obj.popMax()
 */


var MaxHeap = function() {
    this.elements = [];
}

MaxHeap.prototype.push = function(newElement) {
    this.elements.push(newElement);
    let parentIndex = Math.floor( (this.elements.length-2) / 2)
    this.maxHeapify(parentIndex);
}

MaxHeap.prototype.maxHeapify = function(elementIndex) {
    let parentElement = this.elements[elementIndex];
    let leftChild = this.elements[1 + 2*elementIndex];
    let rightChild = this.elements[2*(1+elementIndex)];
    let nextParentIndex = null;
    
    if (parentElement < leftChild) {
        this.swap(elementIndex, 1 + elementIndex*2);
        parentElement = this.elements[elementIndex];
        nextParentIndex = 1 + elementIndex*2;
    }
    if (parentElement < rightChild) {
        this.swap(elementIndex, 2*(1+elementIndex) );
        nextParentIndex = 2*(1+elementIndex);
    }
    
    if (nextParentIndex !== null) {
        return this.maxHeapify(nextParentIndex);
    }
}

MaxHeap.prototype.buildMaxHeap = function() {
    for (let i = 0; i < Math.floor(this.elements.length / 2); i++) {
        this.maxHeapify(i);
    }
}

MaxHeap.prototype.popMax = function() {
    let res = this.elements[0];
    this.elements[0] = -Number.MAX_SAFE_INTEGER;
    this.maxHeapify(0)
    return res === -Number.MAX_SAFE_INTEGER ? null : res;
}

MaxHeap.prototype.swap = function(eleA, eleB)  {
    let temp = this.elements[eleA];
    this.elements[eleA] = this.elements[eleB];
    this.elements[eleB] = temp;
}



// 100th percentile using builtins. 156ms. 
/**
 * initialize your data structure here.
 */
var MaxStack = function() {
    this.stack = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MaxStack.prototype.push = function(x) {
    this.stack.push(x);
};

/**
 * @return {number}
 */
MaxStack.prototype.pop = function() {
    return this.stack.pop()
};

/**
 * @return {number}
 */
MaxStack.prototype.top = function() {
    return this.stack[this.stack.length-1];
};

/**
 * @return {number}
 */
MaxStack.prototype.peekMax = function() {
    return Math.max(...this.stack);
    // Interesting that using ES5 apply method isn't as efficient as spread operator
};

/**
 * @return {number}
 */
MaxStack.prototype.popMax = function() {
    let res = Math.max(...this.stack);
    let indexOfRes = this.stack.lastIndexOf(res);
    this.stack.splice(indexOfRes, 1);
    return res;
};

/** 
 * Your MaxStack object will be instantiated and called as such:
 * var obj = new MaxStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.peekMax()
 * var param_5 = obj.popMax()
 */