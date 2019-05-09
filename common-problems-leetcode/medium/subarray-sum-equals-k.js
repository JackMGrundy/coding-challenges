/* 
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
Accepted
96,129
Submissions
228,367
*/

// 100th percentile. 68 ms
// Once again, maps are the best thing ever
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let sm = 0,
        res = 0,
        matches = new Map();
    matches.set(k, 1);
    
    nums.forEach(num => {
        sm += num;
        if (matches.has(sm)) {
            res += matches.get(sm);
        }
        if ( matches.has(sm+k) ) {
            matches.set(sm+k, matches.get(sm+k)+1);
        } else {
            matches.set(sm+k, 1);
        }
    })
    
    return res;
};