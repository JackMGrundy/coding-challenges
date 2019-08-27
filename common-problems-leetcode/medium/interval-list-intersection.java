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

// 2ms. 99th percentile.
class Solution {
    public int[][] intervalIntersection(int[][] A, int[][] B) {
        if (A.length == 0 || B.length == 0) {
            return new int[0][0];
        }
        int[][] res = new int[A.length + B.length][2];
        
        int iA = 0;
        int iB = 0;
        int iRes = 0;
        int aMin = A[iA][0];
        int aMax = A[iA][1];
        int bMin = B[iB][0];
        int bMax = B[iB][1]; 
        while (iA < A.length && iB < B.length) {

            int minMax = Math.max(aMin, bMin);
            int maxMin = Math.min(aMax, bMax);
            
            if ( maxMin >= minMax ) {
                res[iRes][0] = minMax;
                res[iRes][1] = maxMin;
                iRes++;
            }
            
            if (aMax < bMax) {
                iA++;
                if (iA < A.length) {
                    aMin = A[iA][0];
                    aMax = A[iA][1];
                }
            } 
            else {
                iB++;
                if (iB < B.length) {
                    bMin = B[iB][0];
                    bMax = B[iB][1]; 
                }
            }
        }
        
        return Arrays.copyOfRange(res, 0, iRes);
    }
}