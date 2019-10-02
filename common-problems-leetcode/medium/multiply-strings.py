"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# 128ms. 50 percentile.
# If it's required that you multiply all the digits...one by one
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        output = [ 0 for _ in range(len(num1) + len(num2)) ]
        
        for i, digit1 in enumerate(num1):
            for j, digit2 in enumerate(num2):
                targetIndex = i + j + 1
                output[targetIndex] += int(digit1)*int(digit2)
        
        carry = 0
        for i in range(len(output)-1, -1, -1):
            output[i] += carry
            carry = output[i]//10
            output[i] %= 10
        
        startIndex = 0
        while startIndex < len(output) - 1 and output[startIndex] == 0:
            startIndex += 1
        
        return ''.join([ str(x) for x in output[startIndex:]])


# 40ms. 80 percentile.
# Not sure this is legal...since we just multiply the numbers as ints at the end...
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            return '0'
        
        n1 = 0
        n2 = 0
        numDigitsNum1 = len(num1)
        numDigitsNum2 = len(num2)
        
        for i,num in enumerate(num1):
            n1 += 10**(numDigitsNum1 - i - 1) * (ord(num) - ord('0'))
            
        for i,num in enumerate(num2):
            n2 += 10**(numDigitsNum2 - i - 1) * (ord(num) - ord('0'))
        
        return str(n1 * n2)




"""
Notes:

Consider:
  5432
x 3124

n = length of first num
m = length of second num

Interesting problem actually...the straightforward solution is to do an n by m
calculation where we multiply the least significant digit of the second num times 
each of the digits in the first num, making sure to carry ones along the way...then
repeat this fro each of the digits of the second num. We end one with a 4 numbers,
one for each digit of the second number that we add to get the final answer.

This is an m*n solution...notably it yields the least significant digit first...
and then builds up to the most significant digit


A cool solution that makes this question interesting:

1) https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation

999 * 999 -> 998001
-> Given two terms, the longest the product could be is equal to the length of their
sums. With array indexing this looks like:


So we can preallocate an array with len(nums1) + len(nums2) elements

With basic handwritten multiplication, you multiply each pair of digits. Consider

      2 3
x     5 6
---------
      1 8
    1 2
  
    1 5
  1 0
 ----------
  1 2 8 8       

  - - - -
  0 1 2 3 

The 1's are carry's. 

Now the indices of the digits of the two terms:

2 3
5 6
- -
0 1

Now let's say we're considering the ith digit of the first number and the jth digit
of the second number. When we multiply them, the ones digit of the result goes
to index i + j + 1 in the final array, while the carry (if there is one), goes to
the index i + j. 

Now the problem is super straightforwards. 

This can seem mysterious but it's just born from initializing the final list to have
length equal to the sum of the component lengths. Consider:

      9 9 9
x     9 9 9
        8 1
      8 1
    8 1
      8 1
    8 1
  8 1
    8 1
  8 1
8 1

9 9 8 0 0 1       
_ _ _ _ _ _
0 1 2 3 4 5

again, let i by the ith digit in the first number and j be the jth digit in the second number.

For the intuition, consider that we want the carry digit of the product of the most significant digit to map to element
0 in the final array. i + j = 0
Similarly, we want the ones digit of the product of the least significant digits to map to the last element in the array. In this case, 
i and j will each be equal to 1 - the length of their array, so i + j + 1 gets you to the last element. 
Now for all the in between's consider that increasing i or j by one is equivalent to considering a number that is an order of magnitude
smaller...and appropriately, we also increase the target index by 1, which decreases its significance by an order of magnitude. 

Said differently, every digit of significance we add is like multiplying by 10...which increases the output product by a digit of 
significance too...So it makes sense that the product of the most significant digits would get you to the most significant digit
in the output...and for every decreae in order of significance of either number, we decrease the output too. 

Other examples:

      1 0
x     1 0
---------
        0
      0
    1 0
 ----------
  0 1 0 0      

  - - - -
  0 1 2 3 


      1 2
x       9
---------
      1 8
      9
 ----------
    1 0 8      

    - - -
    0 1 2



Also see the veda multiplications methods
"""
