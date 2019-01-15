#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque 


class node():
    def __init__(self, index, value):
        self.value = value
        self.index = index
        self.children = set()
        self.parent = None
        self.subtreeValue = 0

def cutTheTree(data, edges):
    # List of nodes
    nodes = [node(i, val) for (i, val) in zip(range(len(data)), data)]
    # Children of nodes
    for edge in edges:
        a, b = edge
        nodes[a-1].children.add(nodes[b-1])
        nodes[b-1].children.add(nodes[a-1])
    
    root = nodes[0]
    q = deque([root])
    orderedNodes = [root]

    # DFS to get ordering of nodes
    while q:
        cur = q.popleft()
        # First node that is encountered in a pairing is the parent
        for c in cur.children:
            c.parent = cur
            c.children.remove(cur)
            q.append(c)
            orderedNodes.append(c)

    # Get subtree totals
    orderedNodes.reverse()
    for n in orderedNodes:
        n.subtreeValue += n.value + sum(c.subtreeValue for c in n.children)
    
    midValue = nodes[0].subtreeValue / 2.0
    bestSplit = nodes[0].subtreeValue
    for n in nodes[1:]:
        splitValue = 2 * abs(midValue-n.subtreeValue)
        if splitValue < bestSplit:
            bestSplit = splitValue

    return(int(bestSplit))


if __name__=="__main__":
    data = [100, 200, 100, 500, 100, 600]
    edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
    res = cutTheTree(data, edges)
    print(res)