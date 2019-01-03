#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findMedian function below.
def findMedian(arr):
    arr.sort()
    # Middle element if odd length. Else average of two middlemost elements. 
    result = arr[math.floor(len(arr)/2.0)] if len(arr)%2==1 else (arr[math.floor(len(arr)/2.0)] + arr[math.ceil(len(arr)/2.0)])/2.0
    return(int(result))

if __name__ == '__main__':
    arr = [0, 1, 2, 4, 6, 5, 3]
    result = findMedian(arr)
    print(result)