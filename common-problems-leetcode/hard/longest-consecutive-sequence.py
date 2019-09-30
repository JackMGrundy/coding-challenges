"""
Given an unsorted array of integers, find the length of the longest 
consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
"""
# 64ms. 81 percentile. 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        
        s = set(nums)
        longestStreak = 1
        for num in nums:
            if num - 1 not in s:
                curStreak = 1
                while num + 1 in s:
                    num += 1
                    curStreak += 1
                
                longestStreak = max(longestStreak, curStreak)
        return longestStreak

"""
Notes:
Add each value to a set so we can check if a num exists in constant time.
Then we iterate through the nums. We only proces the "starts" of chains.
We easily check if a num is a start by checking if the preceding num is in
the set. Then its a simple process of incrementing and checking. 

"""