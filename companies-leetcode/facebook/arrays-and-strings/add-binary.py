"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Edge case:
a = "111"
b = "111"
   "1110"
"""
a = "1010"
b = "1011"

# Attempt #1: 91st percentile
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a); a.reverse()
        b = list(b); b.reverse()

        # Padding
        if len(a)<len(b):
            a += [ "0" for x in range(len(b)-len(a)) ]
        elif len(b)<len(a):
            b += [ "0" for x in range(len(a)-len(b)) ]

        res = []
        carry = 0
        for ax, bx in zip(a, b):
            if ax == "1": carry += 1 
            if bx == "1": carry += 1
            
            # carry can be 0, 1, 2, 3
            if carry == 0:
                res.append("0")
                carry = 0
            elif carry == 1:
                res.append("1")
                carry = 0
            elif carry == 2:
                res.append("0")
                carry = 1
            elif carry == 3:
                res.append("1")
                carry = 1

        if carry == 1:
            res.append("1")
        
        res.reverse()

        return(''.join(res))

s = Solution()
res = s.addBinary(a, b)
print(res)



#Attempt 2: 100th percentile (using builtin functions)
class Solution(object):
    def addBinary(self, a, b):
        a = int(a, base=2)
        b = int(b, base=2)
        return(bin(a+b)[2:])