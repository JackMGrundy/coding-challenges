/*
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
*/

// DP method. O(m * (nums.length)^2)
// 20ms. 29th percentile. 
class Solution {
    public int splitArray(int[] nums, int m) {
        int[][] dp = new int[nums.length+1][m+1];
        for (int i = 0; i < nums.length+1; i++) {
            for (int j = 0; j < m+1; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        
        int[] cumSums = new int[nums.length+1];
        for (int i = 0; i < nums.length; i++) {
            cumSums[i+1] = cumSums[i] + nums[i];
        }
        
        dp[0][0] = 0;
        for (int i = 1; i < nums.length+1; i++) {
            for (int j = 1; j < m+1; j++) {
                for (int k = 0; k < i; k++) {
                    dp[i][j] = Math.min(dp[i][j], Math.max(cumSums[i]-cumSums[k], dp[k][j-1]));
                }
            }
        }
        
        return dp[nums.length][m];
    }
}




// 1ms. 61st percentile.
// Note the commented out stream operators.
// I've been excited about streams but they just killed the performance here.
// Using those lines drops the performance to 34ms instead of 1ms. 
import java.util.*;
class Solution {
    public int splitArray(int[] nums, int m) {
        // long l = Arrays.stream(nums).max().getAsInt();
        // long r = Arrays.stream(nums).sum();
        long l = 0;
        long r = 0; 
        for (int num : nums) {
            l = Math.max(l, num);
            r += num;
        }
        int minValidSum = Integer.MAX_VALUE;
        
        while (l <= r) {
            int s = (int) Math.floor((l+r)/2.0);
            
            if (sumIsValid(nums, s, m)) {
                minValidSum = Math.min(minValidSum, s);
                r = s-1;
            } else {
                l = s+1;
            }
        }
        
        return minValidSum;
    }
    
    public boolean sumIsValid(int[] nums, int s, int m) {
        int currentTotal = 0;
        
        for (int num : nums) {
            if (currentTotal + num <= s) {
                currentTotal += num;
            } else {
                if (--m == 0) {
                    return false;
                }
                currentTotal = num;
            }
        }
        return true;
    }
}