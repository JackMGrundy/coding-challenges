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
import java.util.Map;
import java.util.HashMap;
// 98th percentile. 13ms
class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int sm = 0;
        Map<Integer, Integer> matches = new HashMap<Integer, Integer>();
        matches.put(k, 1);
        
        for (int x : nums) {
            sm += x;
            if (matches.containsKey(sm)) {
                res += matches.get(sm);
            }
            
            if (!matches.containsKey(sm+k)) {
                matches.put(sm+k, 1);
            } else {
                matches.put(sm+k, matches.get(sm+k)+1);
            }
        }
        
        return res;
    }
}