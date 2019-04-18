"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
nums = [0,1,0,3,12]
output = [1,3,12,0,0]

# Attempt #1: 100th percentile
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numZeroes = 0
        for counter, val in enumerate(nums):
            if val==0:
                numZeroes += 1
            else:
                nums[counter-numZeroes] = val
        
        nums[ len(nums)-numZeroes:len(nums) ] = [ 0 for x in range(numZeroes) ]

        return(nums)

s = Solution()
res = s.moveZeroes(nums)
print(res)