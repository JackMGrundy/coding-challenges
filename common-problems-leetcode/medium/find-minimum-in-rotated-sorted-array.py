"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
Accepted
323.9K
Submissions
742.6K
"""

# 48ms. 74 percentile.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            m = left + (right - left)//2

            if nums[m] > nums[m+1]:
                return nums[m+1]
            
            # The left section is sorted
            if nums[left] <= nums[m]:
                left = m + 1
            # The right section is sorted
            else:
                right = m - 1
        
        return m