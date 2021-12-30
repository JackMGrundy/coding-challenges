/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

#include <vector>
#include <set>
#include <unordered_set>

// 1st attempt
// 6th percentile
class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::set<int> set(nums.begin(), nums.end());
        return set.size() != nums.size();
    }
};


// 2nd attempt
// 20th percentile
class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> set;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            if (set.find(nums[i]) != set.end()) {
                return 1;
            } 
            set.insert(nums[i]);
        }
        
        return 0;
    }
};

// 30th percentile
class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> set;
        
        for (auto& num : nums) {
            if (set.count(num) != 1) {
                set.insert(num);
            } else {
                return true;
            }
        }
        
        return false;
    }
};


/*
There are "faster solutions" but their asymptotic compleixties are worse...sorting the nums first...
*/