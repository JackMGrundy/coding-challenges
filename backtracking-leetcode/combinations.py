"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
# 1st attempt: 40th percentile in speed
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def bt(n, k, ans):
            if k == 0:
                res.append(ans)
                return []
            
            start = 1 if not ans else ans[-1]+1
            for i in range(start, n+1):
                bt(n, k-1, ans + [i])
        
        res = []
        bt(n, k, [])
        return res
        
        

# 2nd attempt: 49th percentile in speed
# Got a bit of sppedup by working with the same list
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def bt(n, k, ans):
            if k == 0:
                res.append(ans[:])
                return []
            
            start = 1 if not ans else ans[-1]+1
            for i in range(start, n+1):
                ans.append(i)
                bt(n, k-1, ans)
                del ans[-1]
        
        res = []
        bt(n, k, [])
        return res


# 3rd attempt: 51st percentile
# A bit of speedup from using not rather than ==
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def bt(n, k, ans):
            if not k:
                res.append(ans[:])
                return []
            
            start = 1 if not ans else ans[-1]+1
            for i in range(start, n+1):
                ans.append(i)
                bt(n, k-1, ans)
                del ans[-1]
        
        res = []
        bt(n, k, [])
        return res


# 4th attempt: 52nd percentile
# Tiny bit of speedup by changing the placement of the start calculation
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def bt(n, s, k, ans):
            if not k:
                res.append(ans[:])
                return []
            
            for i in range(s, n+1):
                ans.append(i)
                bt(n, i+1, k-1, ans)
                del ans[-1]
        
        res = []
        bt(n, 1, k, [])
        return res


# 5th attempt: 88th percentile
# The big speedup came from adjusting the looping range.
# I also converted bt to a class function...but that didn't
# make a difference
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n: return
        
        res = []
        self.bt(n, 1, k, [], res)
        return res
        
    def bt(self, n, s, k, ans, res):
        if not k:
            res.append(ans)
            return

        for i in range(s, n-k+2):
            self.bt(n, i+1, k-1, ans + [i], res)
        
        
        