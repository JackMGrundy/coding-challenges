#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from queue import Queue

# Complete the steadyGene function below.
def steadyGene(gene):
    s = list(gene)
    freqs = Counter(s)
    check = list(freqs.values())
    if (check[1:]==check[:-1]): return(0)
    
    target = sum(freqs.values())/4
    for k, v in freqs.items(): freqs[k] = int(freqs[k] - target)
    
    checker = {k:v for k, v in freqs.items() if v>0}
    targets = list(checker.keys())
    q = Queue()
    let = ""
    answers = []
    start = 0

    for i in range(len(s)):
        let = s[i]
        if let in targets:
            checker[let] -= 1
            q.put(i)
            while max(checker.values())<=0:
                start = q.get()
                startLet = s[start]
                answers.append(i-start+1)
                checker[startLet] += 1

    return(min(answers))