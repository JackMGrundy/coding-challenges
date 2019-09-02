"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
# 36ms. 90th percentile.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        twoPointer = len(nums)-1
        cur = 0
        zeroPointer = 0
        
        while zeroPointer <= cur <= twoPointer:
            if nums[cur] == 0:
                nums[cur], nums[zeroPointer] = nums[zeroPointer], nums[cur]
                cur += 1
                zeroPointer += 1
            
            elif nums[cur] == 1:
                cur += 1
            
            elif nums[cur] == 2:
                nums[twoPointer], nums[cur] = nums[cur], nums[twoPointer]
                twoPointer -= 1


"""
Notes:

The key here is that there are only 3 values. We can just keep track of pointers to 3 different sections...
swap as needed as we run through.

Makes sense that this is so similar to quick sort (the quintessential in place sorting algo)
"""