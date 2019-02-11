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
# First attempt - very slow
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import copy
        
        res = set()
        stack = [ ]
        for c in candidates:
            stack.append([c])
        
        while stack:
            cur = stack.pop()
            s = sum(cur)
            
            if s==target:
                cur.sort()
                res.add(tuple(cur))
            elif s<target:
                for c in candidates:
                    nxt = copy.deepcopy(cur)
                    nxt.append(c)
                    stack.append(nxt)         
        
        res = [ list(r) for r in res ]
        return(res)
                    
            
# Better solution - very fast
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def helper(remain, stack):
            if remain==0:
                res.append(stack)
                return
                
            for c in candidates:
                if (c > remain): 
                    break
                # Avoids duplicates such as [2, 2, 3] and [2, 3, 2]
                if stack and c < stack[-1]: 
                    continue
                else: 
                    helper(remain - c, stack + [c])
        
        
        helper(target, [])
        return(res)
