/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
*/

#include <iostream>
#include <vector>

class Solution {
public:
    int trap(std::vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int leftMaxHeight = 0;
        int rightMaxHeight = 0;
        int trappedWater = 0;
        
        while (left <= right) {
            
            if (leftMaxHeight < height[left]) {
                leftMaxHeight = height[left];
            } 
            if (rightMaxHeight < height[right]) {
                rightMaxHeight = height[right];
            }
            
            if (leftMaxHeight <= rightMaxHeight) {
                trappedWater += leftMaxHeight - height[left];
                left++;
            } else {
                trappedWater += rightMaxHeight - height[right];
                right--;
            }       
        }
            
        return trappedWater;
    }
};

int main(int argc, const char* arvv[] ) 
{
    Solution s;
    std::vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int answer = s.trap(height);
    std::cout << answer << "\n";
}