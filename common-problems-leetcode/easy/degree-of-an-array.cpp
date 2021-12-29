/*
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
*/
#include <unordered_map>
#include <vector>


// 85th percentile
class Solution {
public:
    int findShortestSubArray(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        std::unordered_map<int, int> firstAppearance;
        std::unordered_map<int, int> lastAppearance;
        int maxDegree = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i];
            counts[val] += 1;
            maxDegree = std::max(maxDegree, counts[val]);
            lastAppearance[val] = i;
            if (firstAppearance.find(val) == firstAppearance.end()) {
                firstAppearance[val] = i;
            }
        }

        int minRange = nums.size();
        for (auto& valCount : counts) {
            int val = valCount.first;
            int count = valCount.second;
            if (count == maxDegree) {
                int range = lastAppearance[val] - firstAppearance[val] + 1;
                minRange = std::min(minRange, range);
            }
        }
        
        return minRange;
    }
};



/*
Great question for practice iterating through maps in c++
*/