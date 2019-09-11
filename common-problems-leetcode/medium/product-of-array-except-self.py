"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# 140ms. 65 percentile.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [ x for x in nums ]
        for i in range(1, len(nums)):
            output[i] *= output[i-1]
        
        output = output
        rollingTotal = 1
        for i in range(len(output)-1, 0, -1):
            output[i] = output[i-1]*rollingTotal
            rollingTotal *= nums[i]
        output[0] = rollingTotal
        
        return output

"""
Notes:

Consider the example:
[1,2,3,4]

We initialize the output array to be a rolling product of these numbers:
[1 2 6 24]

Then we iterate backwards through this array and maintain a rolling product constant comprised of elements from the original array.
For each element, we have the product of the all the elements before it contained in the preceding element. And we have the product
of all the elements after it in the array contained in our constat. Ojala, everything we need to fill each element
"""