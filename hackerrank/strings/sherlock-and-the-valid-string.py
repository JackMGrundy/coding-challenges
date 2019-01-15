#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s = list(s)
    chars = {c:0 for c in s}
    for c in s:
        chars[c] += 1
    counts = {v:0 for k, v in chars.items()}
    for k, v in chars.items():
        counts[v] += 1

    countsKeys = list(counts.keys())
    countsValues = list(counts.values())

    if len(countsKeys) > 2:
        return("NO")
    if len(countsKeys) == 1:
        return("YES")
    if counts[min(countsKeys)]==1 and min(countsKeys)==1:
        return("YES")
    if (max(countsKeys)-min(countsKeys))>1:
        return("NO")
    if (counts[max(countsKeys)] > 1):
        return("NO")

    return("YES")