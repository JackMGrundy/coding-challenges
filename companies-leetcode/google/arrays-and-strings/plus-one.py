"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
# 99th percentile
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            if digits[i] < 10:
                return digits
            else:
                carry = digits[i] - 9
                digits[i] = 0
        return [1] + digits


# 99th percentile. Obnoxious 1-liner
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [ int(x) for x in list(str((1+sum([ x*(10**(len(digits)-1-i)) for i,x in enumerate(digits) ]))))]
        