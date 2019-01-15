#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    weights = {key:(ord(key)-96) for key in set(s.strip())}
    answers = {query:"No" for query in queries}

    curSeq = list(s[0:1])
    weight = weights[curSeq[0]]*len(curSeq)
    if weight in answers.keys():
        answers[weight] = "Yes"

    for nextChar in s[0:]:
        if nextChar == curSeq[0]:
            curSeq.append(nextChar)
        else:
            curSeq = list(nextChar)
        weight = weights[curSeq[0]]*len(curSeq)
        if weight in answers.keys():
            answers[weight] = "Yes"
    answersList = []

    for query in queries:
        answersList.append(answers[query])
    return(answersList)


# uniWeights = [weights[seq[0:1]]*len(seq) for seq in subseqs]

    answers = []

    for query in queries:
        if query in uniWeights:
            answers.append("Yes")
        else:
            answers.append("No")
    return(answers)
    

if __name__ == '__main__':
    s = 'abccddde'
    queries = [1, 3, 12, 5, 9, 10]
    res = weightedUniformStrings(s, queries)
    print(res)