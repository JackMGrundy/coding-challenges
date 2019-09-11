"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
# 44ms. 94th percentile. 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.rotatedBinarySearch(nums, target)
    
    def rotatedBinarySearch(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left <= right:
            m = left + (right - left)//2
            
            if nums[m] == target:
                return m
            
            # Left hand side is sorted normally
            if nums[0] <= nums[m]:
                if nums[0] <= target <= nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            # Right hand side is sorted normally
            else:
                if nums[m] <= target <= nums[-1]:
                    left = m + 1
                else:
                    right = m - 1
        
        return -1


"""
Notes:
The key idea: With normal binary search, we can assume that the entire array is sorted.
We can't assume that here. However, no matter where the pivot is, if we pick a middle point
between the left and right hand sides (l and r), we can guarantee that l to m or m to r is a 
"normal", sorted section. Therefore, we can check if target is in that section. If it is, we
narrow our search to it. If not, it must in the other side. 

"""