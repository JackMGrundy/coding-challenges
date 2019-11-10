/*

Given an array A of non-negative integers, return the maximum sum of elements in
two  non-overlapping  (contiguous)  subarrays, which have lengths L and M.  (For
clarification,  the  L-length  subarray could occur before or after the M-length
subarray.)                                                                      

Formally,  return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) +
(A[j] + A[j+1] + ... + A[j+M-1]) and either:                                    

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or                               

0 <= j < j + M - 1 < i < i + L - 1 < A.length.                                  

                                                                                

Example 1:                                                                      

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2                                    

Output: 20                                                                      

Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length
2.                                                                              

Example 2:                                                                      

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2                                    

Output: 29                                                                      

Explanation:  One  choice  of subarrays is [3,8,1] with length 3, and [8,9] with
length 2.                                                                       

Example 3:                                                                      

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3                                  

Output: 31                                                                      

Explanation:  One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with
length 3.                                                                       

                                                                                

Note:                                                                           

L >= 1                                                                          

M >= 1                                                                          

L + M <= A.length <= 1000                                                       

0 <= A[i] <= 1000                                                               


*/

// 0ms. 100th percentile.
class Solution {
    public int maxSumTwoNoOverlap(int[] A, int L, int M) {
        for (int i = 1; i < A.length; i++) {
            A[i] += A[i - 1];
        }
        int res = A[L + M - 1];
        int Lmax = A[L - 1];
        int Mmax = A[M - 1];
        
        for (int i = L + M; i < A.length; i++) {
            Lmax = Math.max(Lmax, A[i - M] - A[i - M - L] );
            Mmax = Math.max(Mmax, A[i - L] - A[i - M - L] );
            res = Math.max(res, Math.max(Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]));
        }

        return res;
    }
}
/*

Notes:

Prefix sums are the key here. The core logic is:

Iterate through each position in the array. Take a stretch of L cells starting
at that position to be the L sum. The best you can do here is the L Sum plus
the best M length stretch before or after the L stretch. 

The question is then how do we do this efficiently? 

Key note...instead of thinking of it as shifting the L stretch
and identifying the best M stretch before or after, at each point
identify the value of the L stretch AND the M stretch. Meanwhile
keep track of the best L and M stretches seen so far...then the
best we can do at each point is equal to:
max( L stretch + best M stretch seen so far, M stretch + best L stretch seen so far )

To get the current L and M stretches we can use a prefix sum array. 

Boom.

*/