"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1: return(False)
        
        children = defaultdict(list)
        for a, b in edges:
            children[a].append(b)
            children[b].append(a)
        
        visited = [0 for x in range(n)]
        stack = [(0, None)]
        while stack:
            curNode, parent = stack.pop()
            
            for c in children[curNode]:
                if visited[c] and c != parent: return(False)
                if c != parent: stack.append((c, curNode))
            
            visited[curNode] = 1
            
        return(sum(visited)==n)

