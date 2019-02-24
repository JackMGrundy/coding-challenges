#!/bin/python3
"""
https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
A gene is represented as a string of length  (where  is divisible by ), composed of the letters , , , and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

As an example, consider . The substring  just before or after  can be replaced with or . One selection would create .

Function Description

Complete the  function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

steadyGene has the following parameter:

gene: a string
Input Format

The first line contains an interger  divisible by , that denotes the length of a string . 
The second line contains a string  of length .

Constraints

 is divisible by 
Subtask

 in tests worth  points.
Output Format

Print the length of the minimum length substring that can be replaced to make  stable.

Sample Input

8  
GAAATAAA
Sample Output

5
Explanation

One optimal solution is to replace  with  resulting in . 
The replaced substring has length 
"""

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