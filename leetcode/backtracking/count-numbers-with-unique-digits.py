"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""
# 1st attempt: 5th percentile
# Actually used a backtracking approach
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        
        def bt(x):
            nonlocal res
            if len(x)==n:
                return
            
            for i in range(0, 10):
                if len(x)==1 and i==0:
                    continue
                
                if i not in visited:
                    res += 1
                    visited.add(i)
                    bt(x + [i])
                    visited.remove(i)
                    
            
            
        visited = set()
        res = 0
        bt([])
        return res

# 2nd attempt: 72nd percentile in speed
# Arithmetic approach
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def bt(x):
            if x == 0: return 0 
            ans = 9
            for i in range(x-1):
                ans *= (9-i)
            return ans + bt(x-1)
        
        
        return 1 + bt(n)

# 3rd: 72nd percentile/
# Same approach as 2nd attempt, but a bit cleanr
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        ans = 9
        for i in range(n-1):
            ans *= (9-i)
        return ans + self.countNumbersWithUniqueDigits(n-1)