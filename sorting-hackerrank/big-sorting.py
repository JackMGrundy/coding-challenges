#!/bin/python3

import math
import os
import random
import re
import sys
import json

# Complete the bigSorting function below. Takes in a list of numbers as strings, sorts them, returns as strings.
def bigSortingNaive(unsorted):
    unsorted = [int(x) for x in unsorted]
    unsorted.sort()
    # Challenge requires that a list of string be returned
    unsorted = [str(x) for x in unsorted]
    return(unsorted)

def bigSorting(unsorted):
    unsorted.sort(key=int)
    return(unsorted)


if __name__ == '__main__':
    unsorted = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
    result = bigSortingNaive(unsorted)

    # Read in test case
    cwd = os.path.dirname(os.path.realpath(__file__))
    testCases = os.path.join(cwd, "test-cases")
    testCase = os.path.join(testCases, "big-sorting-3.txt")
    with open(testCase) as f:
        testList = json.load(f)
    result = bigSorting(testList)
    print(result)

