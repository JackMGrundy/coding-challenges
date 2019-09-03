/*
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
*/

// 52ms. 97th percentile.
/**
 * @param {number[]} nums
 * @return {number}
 */


var binarySearch = function(arr, l, r, target) {
    while (l <= r) {
        let m = Math.floor((l+r)/2.0);
        if (arr[m] === target) {
            return m;
        }
        
        else if (arr[m] < target && target < arr[m+1]) {
            return m+1;
        }
        
        else if (arr[m] < target) {
            l = m+1;
        }
        
        else if (target < arr[m]) {
            r = m-1;
        }   
    }
}

var lengthOfLIS = function(nums) {
    let dp = [ -Infinity ];
    
    for (let num of nums) {
        if (num > dp[dp.length-1]) {
            dp.push(num);
        } else {
            let index = binarySearch(dp, 0, dp.length-1, num);
            dp[index] = num;
        }
    }
    
    return dp.length-1;
};