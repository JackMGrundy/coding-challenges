"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

# 32ms. 98th percentile.
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self._backtrack(s, 0, "", res)
        return res
    
    def _backtrack(self, s, blocksFormed, path, res):
        if blocksFormed == 4:
            if len(s) == 0:
                res.append(path[:-1])
        else:
            for numDigits in range(1, 4):
                if numDigits <= len(s):
                    if numDigits == 1:
                        self._backtrack(s[numDigits:], blocksFormed + 1, path + s[0:numDigits] + ".", res)
                    elif numDigits == 2 and s[0] != "0":
                        self._backtrack(s[numDigits:], blocksFormed + 1, path + s[0:numDigits] + ".", res)
                    elif numDigits == 3 and s[0] != "0" and int(s[0:3]) < 256:
                        self._backtrack(s[numDigits:], blocksFormed + 1, path + s[0:numDigits] + ".", res)

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