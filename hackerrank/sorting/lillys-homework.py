#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    arrAsc = sorted(arr)
    arrDes = sorted(arr, reverse=True)

    # Dict mapping values to their start locations
    startLocs = {val:index for (val, index) in zip(arr, range(len(arr))) } 
    
    bestSwaps = float("inf")
    # Both ascending and descending order minimize total differences
    for target in [arrAsc, arrDes]:
        numSwaps = 0
        arrCopy = arr.copy()
        startLocsCopy = startLocs.copy()
        # Iterate input list
        for i in range(len(arrCopy)):
            # If element does not match the target element for this index
            if arrCopy[i] != target[i]:
                numSwaps += 1
                # Identify starting index of target element for this index
                correctIndex = startLocsCopy[target[i]]
                # Swap the element in the index with the target element
                arrCopy[i], arrCopy[correctIndex] = arrCopy[correctIndex], arrCopy[i]
                # Update the locations dict
                startLocsCopy[arrCopy[correctIndex]] = correctIndex
        if numSwaps < bestSwaps: bestSwaps=numSwaps
    return(bestSwaps)

if __name__ == '__main__':
    arr = [3, 4, 2, 5, 1]
    res = lilysHomework(arr)
    print(res)