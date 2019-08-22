/* 
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
*/ 


// 88ms. 88th percentile.
/**
 * Initialize your data structure here.
 * @param {number} size
 */
var MovingAverage = function(size) {
    this.size = size;
    this.queue = [];
    this.average = 0.0;
};

/** 
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function(val) {
    let currentValue = this.average*this.queue.length;
    let removed = 0;
    if (this.queue.length === this.size) {
        removed = this.queue.shift();
    }
    this.queue.push(val);
    
    this.average = (currentValue + val - removed) / this.queue.length;
    return this.average;
};

/** 
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */