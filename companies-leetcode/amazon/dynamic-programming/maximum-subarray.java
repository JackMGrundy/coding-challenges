/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/
// 1st attempt: 1ms. 88th percentile.
class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int temp = nums[0];
        for(int i = 1; i < nums.length; i++) {
            temp = Math.max(nums[i], nums[i]+temp);
            res = Math.max(res, temp);
        }
        return res;
    }
}