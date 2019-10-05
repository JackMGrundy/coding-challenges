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
class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0]*(n + 1)
        dp[0:3] = [1, 1, 2]
        
        for i in range(3, n + 1):
            left, right, total = 0, i - 1, 0
            while left < i:
                total += dp[left]*dp[right]
                left += 1
                right -= 1
            dp[i] = total
        
        return dp[-1]
            
"""
Notes:


Intuition is the for any given n, one node is the root and then we can have

0 nodes on the left      /      n - 1 nodes on the right
1 node on the left       /      n -2 nodes on the right
                    .
                    .
                    .

and so on. 

The total number of structures is the sum over levels of
(nodes on left)*(nodes on right)

n:
1 -> 1
2 -> 2
3 -> 5
4 -> ?

n = 2



one node for the root...
+   1 ~ 2  = 2
+   2 ~ 1  = 2
+   3 ~ 0  = 5
+   0 ~ 3  = 5
             --
             14
"""