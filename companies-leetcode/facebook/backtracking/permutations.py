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
# Builtins. 90th percentile in speed. 
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return(list(permutations(nums)))


# 44ms. 91 percentile. Backtracking.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = collections.deque(nums)
        permutationLength = len(nums)
        permutations = []
        
        def helper(permutation):
            if len(permutation) == permutationLength:
                permutations.append(permutation)
                return
            
            for i in range(len(nums)):
                temp = nums.popleft()
                helper(permutation + [temp])
                nums.append(temp)
        
        helper([])
        return permutations


"""
Notes:

Standard  backtracking  problem. This solution uses a deque. Intuitively, at the
very first call, we spin up a recusrive call with all the nums                  
as  options  except  the  first  one,  which  has  already  been  appended  to a
permutation...after doing all those recursive calls, we'll finally get back to  
the  first level, add back that first element, and then do it all again but with
the second element as the first one selected. This kind of process              
is repeated at every level.                                                    

By using a deque, we can ensure that we repeatedly cycle through all the elements
in the same order...we pop elements form the left and append on the right.      

"""
        