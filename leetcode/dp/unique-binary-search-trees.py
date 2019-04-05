"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# First attempt: 64th percentile in speed.
# O(N^2) speed, O(N) space
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        dp = { 0: 1, 1: 1}
        
        for i in range(2, n+1):
            temp = 0
            l = 0
            r = i-1
            
            while r >= 0:
                temp += dp[l]*dp[r]
                l+=1; r-=1
            
            dp[i] = temp
        
                
        return dp[n]

# Attempt 2: 64th percentile in speed.
# Caching doesn't speed things up
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        dp = { 0: 1, 1: 1}
        cache = { (0, 1): 1, (1, 0): 1 }
        
        for i in range(2, n+1):
            temp = 0
            l = 0
            r = i-1
            
            while r >= 0:
                if (l, r) in cache:
                    temp += cache[ (l, r) ]
                else:
                    temp += dp[l]*dp[r]
                    cache[ (l,r) ] = cache[ (r,l) ] = dp[l]*dp[r]
                    
                l+=1; r-=1
            
            dp[i] = temp
        
                
        return dp[n]


# Attempt 3: Still 64th percentile in speed.
# Cutting down the second loop doesn't boost performance
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        dp = { 0: 1, 1: 1}
        
        for i in range(2, n+1):
            temp = 0
            l = 0
            r = i-1
            
            while r >= i//2:
                nxt = dp[l]*dp[r]
                if r!=l: nxt*=2
                temp += nxt
                l+=1; r-=1
            
            dp[i] = temp
        
                
        return dp[n]


# Attempt 4: Still 64th percentile.
# Switching to lists
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            l = 0
            r = i-1
            
            while r >= 0:
                dp[i] += dp[l]*dp[r]
                l+=1; r-=1
            
        
        return dp[n]
                
        

# Attempt 5: Still 64th percentile
# fors
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j]*dp[i-1-j]
        
        return dp[n]


# ....finally looked at the 99th percentile answers. 
# The tip top answer is almost identical to the last one. 
# Leetcode timer is just returning 64th percentile for some reason. 
                
        
        
                
        
        