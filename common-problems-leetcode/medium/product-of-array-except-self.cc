/*
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the 
product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space 
for the purpose of space complexity analysis.)
*/
#include <vector>
#include <iostream>

using namespace std;


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result = nums;
        
        for (int i = 1; i < nums.size(); i++) {
            result[i] *= result[i - 1];
        }
        
        int rollingTotal = 1;
        for (int i = nums.size() - 1; 0 < i; i--) {
            result[i] = result[i - 1]*rollingTotal;
            rollingTotal *= nums[i];
        }
        result[0] = rollingTotal;
        return result;
    }
};


int main(int argc, const char* argv[]) {
    vector<int> nums {1, 2, 3, 4};
    Solution s;
    vector<int> result = s.productExceptSelf(nums);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << ", ";
    }
    cout << "\n";
}