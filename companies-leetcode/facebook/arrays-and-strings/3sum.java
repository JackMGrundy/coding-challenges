/*
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
// 1st attempt: 25ms. 99th percentile
import java.util.Arrays;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> validSums = new ArrayList<List<Integer>>();
        
        for (int first = 0; first < nums.length-2; first++) {
            if (nums[first]>0 || (first > 0 && nums[first]==nums[first-1]) ) {
                continue;
            }
            int second = first+1;
            int third = nums.length-1;
            
            while (second < third) {
                int summed = nums[first] + nums[second] + nums[third];
                
                if (summed < 0) {
                    second++;
                }
                else if (summed > 0) {
                    third--;
                }
                else if (summed == 0) {
                    List<Integer> validSum = new ArrayList<Integer>();
                    validSum.add(nums[first]);
                    validSum.add(nums[second]);
                    validSum.add(nums[third]);
                    validSums.add(validSum);
                    
                    while (second < third && nums[second]==nums[second+1]) {
                        second++;
                    }
                    while (second < third && nums[third]==nums[third-1]) {
                        third--;
                    }
                    second++;
                    third--;
                }
            }
            
        }
        
        return validSums;
    }
}