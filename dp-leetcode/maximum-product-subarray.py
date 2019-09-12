"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
# 60ms. 92 percentile. O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return None
        if len(nums)==1: 
            return nums[0]
        
        curMin = curMax = absMax = nums[0]

        for num in nums[1:]:
            
            if num < 0: curMin, curMax = curMax, curMin
            
            curMin = min( num, num*curMin)
            curMax = max( num, num*curMax)
            
            absMax = max( curMax, absMax )
            
        return absMax



# 48ms. 100 percentile. Favorite answer, although O(N) space. 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        
        return max( nums + reverse )

"""
Notes:

Method 1:
It's about the positives and negatives. Basically keep track of the biggest and smallest product up to the
current num and then act accordingly. 


Method 2:
Intuition: say you have a string of numbers with a single negative in the middle. You are going to achieve
a max sum by multiplying up to that negative on either the left side or the right side.
Now say there are two negatives. Assuming there are positives on either side of the array, you cannot achieve a 
max between the negatives (it will be less than 0). However, assuming you multiply through both of them, it's as 
though they are positive. Therefore, the max will be achieved by multiplying all of the numbers.
Say you have three negatives. This is a combination of the first two scenarios. Using all 3 in a product sticks you with
a negative number. However, taking a product the involes the first two or the last two will yield the largest number.
In all three of these series, if you multiply through from both the left and right side, you're guaranteed to hit
the max product along the way.

This implication holds for 4 negatives, 5, and so (you can make an inductive argument). So it always holds. 

The last complication is 0's. These basically just break the problem into a series if subproblems that still behave as described
above. Therefore, multiplying through from either direction is guaranteed to yield a max answer somewhere along the way. 
"""

