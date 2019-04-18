#!/bin/python3
"""
https://www.hackerrank.com/challenges/maximum-palindromes/problem
Madam Hannah Otto, the CEO of Reviver Corp., is fond of palindromes, or words that read the same forwards or backwards. She thinks palindromic brand names are appealing to millennials.

As part of the marketing campaign for the company's new juicer called the Rotator™, Hannah decided to push the marketing team's palindrome-searching skills to a new level with a new challenge.

In this challenge, Hannah provides a string  consisting of lowercase English letters. Every day, for  days, she would select two integers  and , take the substring  (the substring of  from index  to index ), and ask the following question:

Consider all the palindromes that can be constructed from some of the letters from . You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?

For example, if ,  and , then we have,

image

Your job as the head of the marketing team is to answer all the queries. Since the answers can be very large, you are only required to find the answer modulo .

Complete the functions initialize and answerQuery and return the number of maximum-length palindromes modulo .

Input Format

The first line contains the string .

The second line contains a single integer .

The  of the next  lines contains two space-separated integers ,  denoting the  and  values Anna selected on the  day.

Constraints

Here,  denotes the length of .

Subtasks

For 30% of the total score:

For 60% of the total score:

Output Format

For each query, print a single line containing a single integer denoting the answer.

Sample Input 0

week
2
1 4
2 3
Sample Output 0

2
1
Explanation 0

On the first day,  and . The maximum-length palindromes are "ewe" and "eke".

On the second day,  and . The maximum-length palindrome is "ee".

image

Sample Input 1

abab
1
1 4
Sample Output 1

2
Explanation 1

Here, the maximum-length palindromes are "abba" and "baab".
"""

import math
import os
import random
import re
import sys

# Complete the initialize function below.
def initialize(s):
    # This function is called once before all queries.
    s = list(s)
    factDict = {0:1}
    for i in range(1, 20000): factDict[i] = factDict[i-1]*i


# Complete the answerQuery function below.
def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    mod = 1000000007
    l = max(0, l-1)
    subS = s[l:r]

    # Get char counts - O(N)
    chars = {c:0 for c in subS}
    for c in subS: chars[c] += 1

    if len(chars.keys())==1:
        return(1)

    # Chars available to make first n//2 chars of palindrome - O(N)
    charsAvailable = 0
    for v in chars.values(): charsAvailable += v // 2

    # Get number of possible permutations with repetition
    denom = 1
    for v in chars.values(): denom *= math.factorial(v//2)

    num = math.factorial(charsAvailable)
    perms = num // denom

    # Chars available for use as a middle char - O(N)
    midChars = 0
    for v in chars.values(): 
        if (v%2 > 0): midChars += 1
    if midChars==0: midChars = 1

    maxPals = perms * midChars
    return(maxPals % mod)

