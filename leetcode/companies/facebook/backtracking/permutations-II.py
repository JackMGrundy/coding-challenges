"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
# Attempt 1. 76th percentile in speed
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, vals):
            if len(cur)==len(nums):
                res.append(cur)
            else:
                started = []
                for i, val in enumerate(vals):
                    if val not in started:
                        started.append(val)
                        dfs(cur + [val], vals[0:i] + vals[i+1:] )
        
        dfs([], nums)
        return(res)