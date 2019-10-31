"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0
to node N-1, and return them in any order.                                      

The  graph  is  given  as  follows:  the nodes are 0, 1, ..., graph.length - 1. 
graph[i] is a list of all nodes j for which the edge (i, j) exists.             

Example:                                                                        

Input: [[1,2], [3], [3], []]                                                    

Output: [[0,1,3],[0,2,3]]                                                       

Explanation: The graph looks like this:                                         

0--->1                                                                          

|    |                                                                          

v    v                                                                          

2--->3                                                                          

There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.                               

Note:                                                                           

The number of nodes in the graph will be in the range [2, 15].                  

You  can  print  different  paths in any order, but you should keep the order of
nodes inside one path.                                                          

"""
# 108ms. 99.5 percentile.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = collections.defaultdict(list)
        for start, ends in enumerate(graph):
            for end in ends:
                source[start].append(end)
        

        destination = len(graph) - 1
        queue = collections.deque([ [0] ])
        paths = []
        
        while queue:
            path = queue.popleft()
            currentLocation = path[-1]
            if currentLocation == destination:
                paths.append(path)
            else:
                for neighbor in source[currentLocation]:
                    queue.append( path + [neighbor] )
        
        return paths

"""
Notes:

Straight bfs
"""