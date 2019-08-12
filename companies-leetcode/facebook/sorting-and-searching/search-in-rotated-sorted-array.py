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
# 1st attempt: 63rd percentile in speed

# The key idea: With normal binary search, we can assume that the entire array is sorted.
# We can't assume that here. However, no matter where the pivot is, if we pick a middle point
# between the left and right hand sides (l and r), we can guarantee that l to m or m to r is a 
# "normal", sorted section. Therefore, we can check if target is in that section. If it is, we
# narrow our search to it. If not, it must in the other side. 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        l, r = 0, len(nums)-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m]==target:
                return(m)
            # Is the left hand side a "normal" ordered section
            if nums[l] <= nums[m]:
                # Is target in this "normal section"
                if nums[l] <= target <= nums[m]:
                    # Restrict the search to this section
                    r = m-1
                # The target is not in this section. Switch to searching the other section
                else:
                    l = m+1
            # The right hand side is a "normal" ordered section
            else:
                # Is target in this "normal section"
                if nums[m] <= target <= nums[r]:
                    # Restrict the search to this section
                    l = m+1
                # The target is not in this section. Switch to searching the other section
                else:
                    r = m-1
        
        return -1
                
        
# Second attempt: 
# 1st attempt was 44ms. 99th percentile is 40ms. I looked at a few examples
# that were that fast, and they used the same core idea but had more confusing
# code in my opinion. 




