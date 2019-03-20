/*
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/

// Attempt 1: 79th percentile
// 2 passes. O(N) space and speed
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var rev = nums.slice().reverse();
    for (let i = 1; i < nums.length; i++) {
        nums[i] *= nums[i-1] || 1;
        rev[i] *= rev[i-1] || 1;
    }
    return Math.max( ...nums.concat(rev) );
};



// Attempt 2: 91st percentile in speed
// Single pass. Constant space
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    var min = nums[0],
        max = nums[0],
        curMin = nums[0],
        curMax = nums[0];
    
    for (let i = 1; i < nums.length; i++) {
        let num = nums[i];
        
        if (num < 0) {
            let temp = curMin;
            curMin = curMax;
            curMax = temp;
        }
        
        curMin = Math.min( num, curMin*num );
        curMax = Math.max( num, curMax*num );
        
        min = Math.min(min, curMin);
        max = Math.max(max, curMax);
    }
    
    return max;
};
