/*
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
*/

// First attempt. 65th percentile in speed. 
/**
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {
    let 
        l = 0, 
        res = nums.length+1, 
        sm = 0,
        num = 0;
    
    for (var r = 0; r < nums.length; r++) {
        num = nums[r];
        sm += num;
        while (sm >= s) {
            if (r-l+1 < res) { res=r-l+1; }
            if (r==l) {return 1;}
            sm -= nums[l];
            l += 1;
        }
    }
    
    if (res===nums.length+1) {
        return 0;
    } else {
        return res;
    }
};