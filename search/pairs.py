#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort(reverse=True)

    head = 0
    runner = 1
    res = 0
    while (runner!=len(arr)):
        # if runner==len(arr):
        #     head+=1
        #     runner = head+1
        #     continue     
        diff = arr[head]-arr[runner]
        if diff==k: 
            # res += 1
            # head += 1
            # runner = head+1
            runner += 1
            continue
        if diff<k:
            runner += 1
            continue
        if diff>k:
            head+=1
            # runner = head+1
            continue
    return(res)


if __name__=="__main__":
    k = 2
    arr = [1, 5, 3, 4, 2]
    res = pairs(k, arr)
    print(res)
