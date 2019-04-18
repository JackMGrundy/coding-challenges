"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# 1st attempt: builtin methods. 90th percentile in speed. 
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return(list(permutations(nums)))


# 2nd attempt: actual backtracking with recursive DFS. 60th percentile in speed:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(cur, vals):
            if len(cur)==len(nums):
                res.append(cur)
            else:
                for i, val in enumerate(vals):
                    dfs(cur + [val], vals[0:i] + vals[i+1:] )
        
        dfs([], nums)
        return(res)
        