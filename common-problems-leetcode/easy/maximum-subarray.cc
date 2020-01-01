/*

Given  an  integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.                       

Example:                                                                        

Input: [-2,1,-3,4,-1,2,1,-5,4],                                                 

Output: 6                                                                       

Explanation: [4,-1,2,1] has the largest sum = 6.                                

Follow up:                                                                      

If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.                              

*/
#include <vector>
#include <algorithm>

class Solution {
public:

    int maxSubArray(std::vector<int>& nums) {
        if (nums.size() == 0) return 0;
        
        std::vector<int> dp = nums;
        int maximumContiguousSum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = std::max(dp[i - 1] + nums[i], nums[i]);
            maximumContiguousSum = std::max(maximumContiguousSum, dp[i]);
        }

        return maximumContiguousSum;
    }
};


/*

Notes:

Simple dp problem. Iterate through the vector. At each element, check if we can get a bigger sum
by including the best sum we can get using the sum to the left...

*/