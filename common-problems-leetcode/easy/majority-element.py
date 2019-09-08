"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
# 192ms. 82 percentile.
# question guarantees an answer, so we don't need the check part of boyer moore that is commented out. 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore
        count = 0
        candidate = ""
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # check = 0
        # for num in nums:
        #     if num == candidate:
        #         check += 1
        
        # return candidate if check >= 1 + len(nums)//2 else ""
    
        return candidate



"""
Notes:
See notes on Boyer Moore
"""