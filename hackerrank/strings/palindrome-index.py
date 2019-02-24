#!/bin/python3
"""
Given a string of lowercase letters in the range ascii[a-z], determine a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. For example, if your string is "bcbc", you can either remove 'b' at index  or 'c' at index . If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Function Description

Complete the palindromeIndex function in the editor below. It must return the index of the character to remove or .

palindromeIndex has the following parameter(s):

s: a string to analyze
Input Format

The first line contains an integer , the number of queries. 
Each of the next  lines contains a query string .

Constraints

All characters are in the range ascii[a-z].
Output Format

Print an integer denoting the zero-indexed position of the character to remove to make  a palindrome. If  is already a palindrome or no such character exists, print .

Sample Input

3
aaab
baa
aaa
Sample Output

3
0
-1
Explanation

Query 1: "aaab" 
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 2: "baa" 
Removing 'b' at index  results in a palindrome, so we print  on a new line.

Query 3: "aaa" 
This string is already a palindrome, so we print . Removing any one of the characters would result in a palindrome, but this test comes first.
"""

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    s = list(s)
    left = 0
    right = len(s)-1
    rmIndex = -1
    for i in range(len(s)//2):
        if s[left] != s[right]:
            if s[left] == s[right-1] and s[left+1] == s[right-2]:
                rmIndex = right
                right += -1
            elif s[left+1] == s[right] and s[left+2] == s[right-1]:
                rmIndex = left
                left += 1
            
        left += 1
        right += -1
    return(rmIndex)


if __name__ == '__main__':
    s = 'aaab\nbaa\naaa'
    res = palindromeIndex(s)
    print(res)