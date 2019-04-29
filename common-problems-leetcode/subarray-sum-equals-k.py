"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
Accepted
96,129
Submissions
228,367
"""
# 89th percentile. 56ms. 
from itertools import accumulate
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        res = 0
        matches = defaultdict(int) 
        matches[k] = 1
        
        forward = list(accumulate(nums))

        for x in forward:
            if x in matches:
                res += matches[x] 
            matches[x+k] += 1
        
        return res

# Tried to speed things up by doing the acumulation on the fly, but no dice
# 89th percentile. 56ms. 
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        res = 0
        matches = defaultdict(int) 
        matches[k] = 1
        sm = 0

        for n in nums:
            sm += n
            if sm in matches:
                res += matches[sm] 
            matches[sm+k] += 1
        
        return res