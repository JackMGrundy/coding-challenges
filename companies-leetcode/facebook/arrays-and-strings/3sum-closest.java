/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
// 1st attempt: 5ms. 63rd percentile.
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0]+nums[1]+nums[nums.length-1];
        
        for (int first = 0; first < nums.length-2; first++) {
            if (first > 0 && nums[first]==nums[first-1]) {
                continue;
            }
            int second = first+1;
            int third = nums.length-1;
            
            while (second < third) {
                int summed = nums[first] + nums[second] + nums[third];
                if (summed == target) {
                    return target;
                }
                
                int distanceFromTarget = summed - target;
                if (Math.abs(distanceFromTarget) < Math.abs(closestSum-target) ) {
                    closestSum = summed;
                }
                  
                if (distanceFromTarget < 0) {
                    second++;
                }
                else if (distanceFromTarget > 0) {
                    third--;
                }
                
            }
            
        }
        
        return closestSum;
    }
}


// 2nd attempt. 4ms. 96th percentile.
// Got a little bump from eliminate a Math.abs call
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int closestSum = nums[0]+nums[1]+nums[nums.length-1];
        int smallestDistance = Math.abs(closestSum - target);
        
        for (int first = 0; first < nums.length-2; first++) {
            if (first > 0 && nums[first]==nums[first-1]) {
                continue;
            }
            int second = first+1;
            int third = nums.length-1;
            
            while (second < third) {
                int summed = nums[first] + nums[second] + nums[third];
                if (summed == target) {
                    return target;
                }
                
                int distanceFromTarget = summed - target;
                if (Math.abs(distanceFromTarget) < smallestDistance ) {
                    closestSum = summed;
                    smallestDistance = Math.abs(closestSum - target);
                }
                  
                if (distanceFromTarget < 0) {
                    second++;
                }
                else if (distanceFromTarget > 0) {
                    third--;
                }
                
            }
            
        }
        
        return closestSum;
    }
}