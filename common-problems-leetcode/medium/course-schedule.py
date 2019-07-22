"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
Accepted
226.5K
Submissions
592.5K
"""

# 40ms, 97th percentile in speed
class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        neighbors = self.getNeighbors(numCourses, prerequisites)
        visited = [False] * numCourses
        recStack = [False] * numCourses
        
        for node in range(numCourses):
            if visited[node] == False:
                if self.cycleUtil( node, recStack, visited, neighbors ) == True:
                    return False
        
        return True
    
    
    def cycleUtil(self, node, recStack, visited, neighbors):
        visited[node] = True
        recStack[node] = True
        
        for neighbor in neighbors[node]:
            if recStack[neighbor] == True:
                return True            
            if visited[neighbor] == False:
                if self.cycleUtil( neighbor, recStack, visited, neighbors) == True:
                    return True
        
        recStack[node] = False
        return False
    
    
    def getNeighbors(self, nodes, links):
        res = { node:[] for node in range(nodes) } 
        
        for link in links:
            a, b = link
            res[a].append(b)
        
        return res