/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
// 1st attempt: 67ms. 68th percentile.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort( (a,b) => a-b);
    let closestSum = nums[0]+nums[1]+nums[nums.length-1];
    let smallestDistance = Math.abs(closestSum - target);
    
    for (let first = 0; first < nums.length-2; first++) {
        if (first > 0 && nums[first] === nums[first-1]) {
            continue;
        }
        let second = first+1;
        let third = nums.length-1;
        
        while (second < third) {
            let summed = nums[first] + nums[second] + nums[third];
            
            if (summed === target) {
                return target;
            }
            
            let distanceFromTarget = summed - target;
            if (Math.abs(distanceFromTarget) < smallestDistance) {
                closestSum = summed;
                smallestDistance = Math.abs(closestSum - target);
            }
            
            if (distanceFromTarget < 0) {
                second++;
            }
            else if (distanceFromTarget > 0) {
                third--
            }
        }
    }
    
    return closestSum;
};




// 2nd attempt: 84th percentile. 64ms.
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort( (a,b) => a-b);
    let closestSum = nums[0]+nums[1]+nums[nums.length-1];
    let smallestDistance = Math.abs(closestSum - target);
    
    for (let first = 0; first < nums.length-2; first++) {
        if (first > 0 && nums[first] === nums[first-1]) {
            continue;
        }
        let second = first+1;
        let third = nums.length-1;
        
        while (second < third) {
            let summed = nums[first] + nums[second] + nums[third];
            
            if (summed === target) {
                return target;
            }
            
            let distanceFromTarget = summed - target;
            if (Math.abs(distanceFromTarget) < smallestDistance) {
                closestSum = summed;
                smallestDistance = Math.abs(closestSum - target);
            }
            
            if (distanceFromTarget < 0) {
                second++;
                while (second < third && nums[second] === nums[second-1]) {
                    second++;
                }
            }
            else if (distanceFromTarget > 0) {
                third--;
                while (second < third && nums[third] == nums[third+1]) {
                    third--;
                }
            }
        }
    }
    
    return closestSum;
};