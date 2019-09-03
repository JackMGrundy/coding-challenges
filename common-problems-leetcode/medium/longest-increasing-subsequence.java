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

// 2ms. 71st percentile.
import java.util.*;
class Solution {
    public int lengthOfLIS(int[] nums) {
        
        List<Integer> dp = new ArrayList<Integer>();
        dp.add(Integer.MIN_VALUE);
        
        for (int num : nums) {
            if (num > dp.get(dp.size()-1)) {
                dp.add(num);
            } else {
                int index = Collections.binarySearch(dp, num);
                if (index < 0) {
                    index = -(index + 1);
                }
                dp.set(index, num);
            }
        }
        int res = dp.size()-1;
        return res;
    }
}