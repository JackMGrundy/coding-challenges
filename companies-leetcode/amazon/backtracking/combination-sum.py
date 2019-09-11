"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# 76ms. 65 percentile. 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(remainder, curNumbers):
            if remainder == 0:
                res.append(curNumbers)
                return
            if remainder < 0:
                return
            
            for candidate in candidates:
                if curNumbers and candidate < curNumbers[-1]:
                    continue
                if 0 <= remainder - candidate:
                    dfs(remainder - candidate, curNumbers + [candidate])
        
        dfs(target, [])
        return res


"""
Notes:

The simple part of this problem is doing a backtracking dfs style approach...at each level of recursion, just try subtracting each number in 
the list of candidates. If you get 0, great that's a valid combination. If it's less than 0 quick that line of search. If it's greater than 
0 spin up another level of recusion. 

The tricky part of this problem is dealing with the duplicates bit. My favorite idea so far to accomplish this is the
if curNumbers and candidate < curNumbers[-1]:
    continue

bit.

To understand this, consider this example:
Your input
[2,3,6,7]
7
Output
[[2,2,3],[2,3,2],[3,2,2],[7]]
Expected
[[2,2,3],[7]]

The problem is the:
[2,2,3],[2,3,2],[3,2,2]

that bit of code enforces that we only consider combinations that are montonically increasing. That fixes this instance. 

This is a much better (in terms of speed, memory and arguably readbility) approach than doing something like keeping a set of combinations found so far. 
"""