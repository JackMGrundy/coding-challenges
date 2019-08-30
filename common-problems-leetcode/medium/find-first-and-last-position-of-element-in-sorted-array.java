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

// 0ms. 100th percentile.
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int l = 0;
        int r = nums.length-1;
        int[] res = new int[2];
        res[0] = leftMost(l, r, nums, target);
        res[1] = rightMost(l, r, nums, target);
        return res;
    }
    
    public int leftMost(int l, int r, int[] nums, int target) {
        while (l <= r) {
            int m = (l+r) / 2;
            if ( (m == 0 || nums[m-1] != target) && (nums[m] == target) ) {
                return m;
            } else if (nums[m] < target) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return -1;
    }
    
    public int rightMost(int l, int r, int[] nums, int target) {
        while (l <= r) {
            int m = (l+r) / 2;
            if ( (m == nums.length-1 || nums[m+1] != target) && (nums[m] == target) ) {
                return m;
            } else if (nums[m] <= target) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return -1;
    }
}