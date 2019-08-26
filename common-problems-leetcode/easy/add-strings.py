"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# I think this just means we use ord...

# 44ms. 84th percentile.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res = []
        carry = 0
        while num1 or num2:
            d1 = ord(num1.pop())-ord('0') if num1 else 0
            d2 = ord(num2.pop())-ord('0') if num2 else 0
            
            temp = d1+d2+carry
            carry = temp//10
            res.append(temp % 10)
        
        if carry:
            res.append(carry)
        return ''.join([ str(i) for i in res ])[::-1]
        