"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

# 82nd percentile
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = len(nums)//2
        left, right = 0, len(nums) - 1
        while left <= right:
            val = nums[index]
            if val == target:
                return index
            elif val < target:
                left = index + 1
            elif target < val:
                right = index - 1
            
            index = (left + right)//2
        
        return -1
        

"""
Note the + and - on the elifs....we can eliminate index in those cases...also the -1 on the starting right
"""