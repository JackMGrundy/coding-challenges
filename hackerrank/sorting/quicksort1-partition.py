#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    partition = arr[0]
    left = [x for x in arr if x < partition]
    right = [x for x in arr if x > partition]
    return(left + [partition] + right)


if __name__ == '__main__':
    arr = [4, 5, 7, 3, 2]
    result = quickSort(arr)
    print(result)