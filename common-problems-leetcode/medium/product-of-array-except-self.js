/*
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
*/
// 1st attempt: 100th percentile
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let res = nums.slice();
    for (let i = nums.length-2; i >= 0; i--) {
        nums[i] *= nums[i+1];
    }
    let temp1 = res[0];
    let temp2 = temp1;
    res[0] = nums[1];
    for (i = 1; i < nums.length-1; i++) {
        temp2 = res[i];
        res[i] = temp1 * nums[i+1];
        temp1 *= temp2;
    }
    res[res.length-1] = temp1;
    
    return res;
};