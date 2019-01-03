#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):

    # Preallocate array of x in 0 to 100
    items = list([ "" for i in range(100) ])

    # Loop through elements. Append to correct list based on spot. First half of items are "-"
    for i in range(len(arr)//2):
        items[int(arr[i][0])] += "- "
    
    for i in range(len(arr)-len(arr)//2, len(arr)):
        items[int(arr[i][0])] += str(arr[i][1]) + " "

    # Filter out blanks
    items = [item for item in items if item != ""]

    print("".join(items))


if __name__ == '__main__':
    arr = [['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]
    countSort(arr)