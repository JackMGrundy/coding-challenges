#!/bin/python3

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