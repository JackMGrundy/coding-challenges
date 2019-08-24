/*
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
*/
// 52. 91st percentile.
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let s = new Set();
    let matches = new Set();
    nums1.map( num => s.add(num));
    for (let num of nums2) {
        if (s.has(num)) {
            matches.add(num);
        }
    }
    let res = [];
    for (let num of matches) {
        res.push(num);
    }
    return res;
};