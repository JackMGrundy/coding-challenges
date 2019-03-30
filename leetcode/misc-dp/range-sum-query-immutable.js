/*
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Accepted
131,021
Submissions
353,568
*/

// 1st attempt: 70th percentile in speed
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.nums = nums;
    for (let i = 1; i < nums.length; i++) {
        this.nums[i] += this.nums[i-1];
    }
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    if (i==0) return this.nums[j];
    return this.nums[j]-this.nums[i-1];
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(i,j)
 */


//  2nd attemmpt: 94th percentile in speed...althogh twice as much as space
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.nums = nums;
    this.prefixSums = [nums[0]];
    for (let i = 1; i < nums.length; i++) {
        this.prefixSums[i] = this.prefixSums[i-1]+nums[i];
    }
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.prefixSums[j]-this.prefixSums[i]+this.nums[i];
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(i,j)
 */