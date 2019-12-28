/*
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
*/

#include <unordered_map>
#include <vector>
#include <iostream>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;
        std::vector<int> result;
        
        for (int i = 0; i < nums.size(); i++) {
            if (hash.find(nums[i]) != hash.end()) {
                result.push_back(hash[ nums[i]]);
                result.push_back(i);
                return result;
            }
            
            hash[target - nums[i]] = i;
        }
        
        return result;
    }
};

int main( int argc, const char* argv[] )
{
	Solution s;
    std::vector<int> input = {2,7,11,15};
    int target = 9;

    std::vector<int> result = s.twoSum(input, target);
    std::cout << result[0] << ", " << result[1] << "\n";
}