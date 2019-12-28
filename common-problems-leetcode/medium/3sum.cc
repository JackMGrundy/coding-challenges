/*
Given an array nums of n integers, are there elements a, b, c in 
nums such that a + b + c = 0? Find all unique triplets in the 
array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/

#include <vector> 
#include <algorithm> 
#include <iostream>

// 100ms. 74th percentile.
class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> triplets;
        
        for (unsigned int l = 0; l < nums.size(); l++) {
            if (0 < l && nums[l - 1] == nums[l]) {
                continue;
            }
            
            int m = l + 1, r = nums.size() - 1;
            while (m < r) {
                int s = nums[l] + nums[m] + nums[r];
                if (0 < s) {
                    r--;
                } else if (s < 0) {
                    m++;
                } else {
                    triplets.push_back( std::vector<int> {nums[l], nums[m], nums[r]} );
                    while (m + 1 < r && nums[m] == nums[m + 1]) m++;
                    while (m < r - 1 && nums[r - 1] == nums[r]) r--; 
                    m++;
                    r--;

                }
            } 
        }
        return triplets;
    }
};


int main(int argc, const char* argv[] ) 
{
    Solution s;
    std::vector<int> nums = {-1,0,1,2,-1,-4,1};
    std::vector<std::vector<int>> result = s.threeSum(nums);

    for (int v = 0; v < result.size(); v++) {
        std::cout << "[";
        for (int i = 0; i < result[v].size(); i++) {
            std::cout << result[v][i] << " ";
        }
        std::cout << "]\n";
    }
}