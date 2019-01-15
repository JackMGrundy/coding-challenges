#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    s1 = list(s1)
    s2 = list(s2)

    table = [ [0 for c in ([0] + s2)] for c in ([0] + s1)]

    for r in range(1, len(table)):
        for c in range(1, len(table[0])):
            if s1[r-1]==s2[c-1]: 
                table[r][c]+= (1 + table[r-1][c-1]) 
            elif table[r][c-1]>table[r-1][c]:
                table[r][c] = table[r][c-1]
            else:
                table[r][c] = table[r-1][c]

    return(max(max(table)))