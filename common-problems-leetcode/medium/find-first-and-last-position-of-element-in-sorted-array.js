/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
*/

// 40ms. 100th percentile.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let leftMost = function(l, r, nums, target) {
    while (l <= r) {
        let m = Math.floor( (l+r) / 2.0);
        
        if ( (m === 0 || nums[m-1] !== target) && (nums[m] === target) ) {
            return m;
        }
        else if (nums[m] < target) {
            l = m+1;
        } else {
            r = m-1;
        }
    }
    return -1;
}

let rightMost = function(l, r, nums, target) {
    while (l <= r) {
        let m = Math.floor( (l+r) / 2.0);
        
        if ( (m === nums.length-1 || nums[m+1] !== target) && (nums[m] === target) ) {
            return m;
        }
        else if (nums[m] <= target) {
            l = m+1;
        } else {
            r = m-1;
        }
    }
    return -1;
}


var searchRange = function(nums, target) {
let l = 0;
let r = nums.length-1;
let first = leftMost(l, r, nums, target);
let last = rightMost(l, r, nums, target);
return [first, last];
};