"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from itertools import combinations
# Attempt 1: use built in tools. 100th percentile in speed. 34th percentile in space (11MB vs top score of 10.7MB)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        for i in range(len(nums)+1):
            cs = combinations(nums, i)
            for combination in cs:
                res.append(list(combination))
        return(res)


# Attempt 2: Without built in tools. 100th percentile in speed. 65th percentile in space. 10.9Mb. 
# Much cooler way to solve.
# Logic: start with an empty set. To build up the subsets formed with the first
# num, simply add the only existing set, [], plus 1 = [1]. Keep [].
# To add the second num, once again, just add it to everything already in the list,
# but also keep the originals. Get [[], [1], [2], [1,2]]. Repeat. 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [x+[num] for x in res]
        return(res)

# Attempt 3: Interesting recursive solution. 44th percentile in speed
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, start, lst):
            res.append(lst)
            if depth==len(nums):
                return()
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, lst + [nums[i]])
        
        res = []
        nums.sort()
        dfs(0, 0, [])
        return(res)


if __name__=='__main__':
    nums = [1,2,3]
    s = Solution()
    res = s.subsets(nums)
    print(res)