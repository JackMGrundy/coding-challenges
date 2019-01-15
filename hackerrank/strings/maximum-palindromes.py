#!/bin/python3

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

