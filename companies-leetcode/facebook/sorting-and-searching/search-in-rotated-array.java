/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/

// 1st attempt: 100th percentile in speed. 0ms. 
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        int l = 0;
        int r = nums.length-1;
        while (l <= r) {
            int mid = (l+r) / 2;
            if (target == nums[mid]) {
                return mid;
            }
            
            // left side is monotonically increasing
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target <= nums[mid]) {
                    r = mid-1;
                }
                else {
                    l = mid+1;
                }
            } 
            // right side is monotonically increasing
            else {
                if (nums[mid] <= target && target <= nums[r]) {
                    l = mid+1;
                } 
                else {
                    r = mid-1;
                }
            }
        }
        
        return -1;
    }
}