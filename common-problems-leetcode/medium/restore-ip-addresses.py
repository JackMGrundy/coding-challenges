"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

# 32ms. 98th percentile.
# not super clean but low on time rn...
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12:
            return ""
        ips = []
        s = list(s)
        
        def backTrack(cutoffs, s):
            curIndex = 0 if not cutoffs else cutoffs[-1]
            if len(cutoffs) == 3 and curIndex >= len(s)-3:
                ips.append(cutoffs)
                return
            elif len(cutoffs) >= 3:
                return
            
            for i in range(1,4):
                if s[curIndex] == "0" and i >= 2 :
                    continue
                if len(cutoffs) < 3 and curIndex + i < len(s):
                    backTrack(cutoffs + [curIndex+i], s)
        
        
        def verifyIp(cutoffs):
            last = len(s)
            ip = []
            cutoffs = [0] + cutoffs
            while cutoffs:
                block = s[cutoffs[-1]:last]
                if int(''.join(block)) >= 256:
                    return
                elif block[0] == "0" and len(block) > 1:
                    return
                else:
                    ip = block + ["."] + ip if ip else block
                last = cutoffs.pop()
            res.append(''.join(ip))

        
        backTrack([], s)
        res = []
        for ip in ips:
            verifyIp(ip)

        return res



"""
Note that given that a valid IP can be at most 12 digits and
have at most 4 sections, there are only so many combinations
of valid period placements. We can just generate those combinations
for the length of s and then check if they're valid.

The one wrinkle is no blocks that start with 0 but have length
greater than 1.
"""