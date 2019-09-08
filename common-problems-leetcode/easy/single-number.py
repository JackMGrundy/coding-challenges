"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

# 96ms. 88th percentile.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total ^= num
        return total
            

"""
Notes:

XOR makes this possible without extra space. If two numbers are the same, XOR returns 0...their bits will line up
perfectly, so they will cancel out. 

The confusing part is how does it work out to XOR a string of numbers...the answer is that XOR is associative. 

a XOR (b XOR c) and (a XOR b) XOR c are the same...
"""