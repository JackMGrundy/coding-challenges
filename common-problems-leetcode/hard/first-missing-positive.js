/*
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
*/
// 56ms. 74th percentile.
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    if (nums === null || nums.length === 0) {
        return 1;
    }
    nums = [0].concat(nums);
    let minPositiveValue = nums.reduce( (a,b) => {
        if (0 < b && b < a) {
            return b;
        }
        return a;
    }, Infinity);
    console.log(minPositiveValue);
    
    if (minPositiveValue > 1) {
        return 1;
    }
    
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        if (num < 0) {
            continue
        }
        else if (num === i) {
            continue;
        }
        else if (0 < num && num < nums.length) {
            nums[i] = -1;
            while (0 < num && num < nums.length) {
                if (nums[num] === num) {
                    break;
                }
                let temp = nums[num];
                nums[num] = num;
                num = temp;
            }
        } 
    }
    
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== i) {
            return i;
        }
    }
    return nums.length;
};