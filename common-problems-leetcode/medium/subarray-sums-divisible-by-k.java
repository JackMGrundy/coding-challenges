/*
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
*/

// 22ms. 48th percentile.
// No time to speed up rn...
// If there were time...I'd do the counting and mod parts simultaneously...
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] mods = new int[A.length+1];
        
        for(int i = 0; i < A.length; i++) {
            int temp = (mods[i]+A[i])%K;
            if (temp < 0) {
                temp += K;
            }
            mods[i+1] = temp;
        }
        
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int num : mods) {
            map.put(num, map.getOrDefault(num, 0)+1);
        }
        
        int res = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int val = entry.getValue();
            res += val*(val-1)/2;
        }
        
        return res;
    }
}