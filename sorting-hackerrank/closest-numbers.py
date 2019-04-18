#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    diffs = [abs(x1 - x2) for (x1, x2) in zip(arr[0:len(arr)-1], arr[1:])]
    minDiff = min(diffs)

    # Account for possibility of multiple min difference pairs
    minIndices = [x for x in range(len(diffs)) if diffs[x]==minDiff]

    minPairs = []
    for x in minIndices:
        minPairs.append(arr[x])
        minPairs.append(arr[x+1])

    return(minPairs)
    

if __name__ == '__main__':
    arr = [100, 150, -20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
    result = closestNumbers(arr)
    print(result)