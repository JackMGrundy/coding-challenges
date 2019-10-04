"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

# 32ms. 98th percentile.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        
        def backtrack(ip, index, blocksLeft):
            if blocksLeft == 0:
                if index == len(s):
                    ips.append( ip[0:-1] )
                return
            
            if index < len(s):
                backtrack(ip + s[index] + ".", index + 1, blocksLeft - 1)
            if index + 1 < len(s) and s[index] != '0':
                backtrack(ip + s[index:index+2] + ".", index + 2, blocksLeft - 1)
            if index + 2 < len(s) and s[index] != '0' and int(s[index:index+3]) < 256:
                backtrack(ip + s[index:index+3] + ".", index + 3, blocksLeft - 1)
        
        
        backtrack("", 0, 4)
        
        return ips

"""
Notes:

Each block of the ip can have 1, 2, or 3 digits. Any single digit is allowed.
Any combination of 2 digits is allowed as long as the first isn't a 0. 
Any combination of 3 digits allowed such that the first isn't a 0 and the
total is less than 256.

Given these rules, we use backtracking. 

The stopping condition is that we have formed 4 blocks. If we have, we append
the new ip to the list of results. We're careful not to include the last
period at the very end. 

Otherwise, we try all three ways of adding a new block (1 digit, 2 digits, or 3 digits).
Note we make sure we have enough chars left to actually allocate the number of digits  
"""