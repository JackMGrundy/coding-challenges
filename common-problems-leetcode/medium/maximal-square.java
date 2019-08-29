/*
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
*/

// 4ms. 95th percentile
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) {
            return 0;
        }
        
        int best = 0;
        int prevSquare = 0;
        int[] dp = new int[matrix[0].length+1];
        
        for (int j = 1; j < matrix.length+1; j++) {
            for (int i = 1; i < matrix[0].length+1; i++) {
                int temp = dp[i];
                if (matrix[j-1][i-1] == '1') {
                    dp[i] = Math.min(Math.min(dp[i], dp[i-1]), prevSquare)+1;
                    best = Math.max(best, dp[i]);
                } else {
                    dp[i] = 0;
                }
                prevSquare = temp;
            }
        }
        
        return best*best;
    }
}