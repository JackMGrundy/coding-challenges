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

Intuitively, at the top level we're saying "I'm going to start this process with
the first element as the first element in the permutation, then I'll repeat it
with the second element as the first element, and so on..."
Since we're doing this at every level of recursion, we're going to get all
the permutations. 

Key lesson is we just need a way to ensure that at each level, each element will
get its turn "going first".

Illustration of the recursion:
level: 1, nums: deque([1, 2, 3]), permutation: []
level: 2, nums: deque([2, 3]), permutation: [1]
level: 3, nums: deque([3]), permutation: [1, 2]
level: 4, adding: [1, 2, 3]
level: 2, nums: deque([3, 2]), permutation: [1]
level: 3, nums: deque([2]), permutation: [1, 3]
level: 4, adding: [1, 3, 2]
level: 1, nums: deque([2, 3, 1]), permutation: []
level: 2, nums: deque([3, 1]), permutation: [2]
level: 3, nums: deque([1]), permutation: [2, 3]
level: 4, adding: [2, 3, 1]
level: 2, nums: deque([1, 3]), permutation: [2]
level: 3, nums: deque([3]), permutation: [2, 1]
level: 4, adding: [2, 1, 3]
level: 1, nums: deque([3, 1, 2]), permutation: []
level: 2, nums: deque([1, 2]), permutation: [3]
level: 3, nums: deque([2]), permutation: [3, 1]
level: 4, adding: [3, 1, 2]
level: 2, nums: deque([2, 1]), permutation: [3]
level: 3, nums: deque([1]), permutation: [3, 2]
level: 4, adding: [3, 2, 1]
"""
        