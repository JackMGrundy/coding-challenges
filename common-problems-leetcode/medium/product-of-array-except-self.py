"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# 1st attempt: 42nd percentile in speed. O(N) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        back = nums[:]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            back[i] *= back[i+1]
        res = [0]*len(nums)
        res[0] = back[1]
        res[-1] = nums[-2]
        for i in range(1, len(nums)-1):
            res[i] = nums[i-1] * back[i+1]
        return res

# 2nd attempt: 65th percentile in speed. O(1) space.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[:]
        for i in range(len(nums)-2, -1, -1):
            nums[i] *= nums[i+1]
        
        temp = temp2 = res[0]
        res[0] = nums[1]
        for i in range(1, len(nums)-1):
            temp2 = res[i]
            res[i] = temp * nums[i+1]
            temp *= temp2
        res[-1] = temp
        
        return res

# ...too sleepy to keep going rn