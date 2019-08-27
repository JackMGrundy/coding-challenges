/*
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
*/

// 80ms. 86th percentile.
/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number[][]}
 */
var intervalIntersection = function(A, B) {
    if (A.length === 0 || B.length === 0) {
        return [];
    }
    let aI = 0;
    let bI = 0;
    let res = [];
    while (aI < A.length && bI < B.length) {
        let curA = A[aI];
        let curB = B[bI];
        
        let minMax = Math.min(curA[1], curB[1]);
        let maxMin = Math.max(curA[0], curB[0]);
        
        // There is overlap
        if (minMax >= maxMin) {
            // Overlap
            res.push( [maxMin, minMax] );
        }
        
        // Advance intervals
        if (curA[1] < curB[1]) {
            aI++;
        } else {
            bI++;
        }
    }
    return res;
};