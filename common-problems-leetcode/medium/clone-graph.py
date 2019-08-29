"""

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

 

Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""

# 48ms. 50th percentile. bfs.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNodesToNew = {}
        nodeCopy = Node(node.val, []) 
        oldNodesToNew[node] = nodeCopy
        res = nodeCopy
        q = collections.deque([node])
        while q:
            head = q.popleft()

            for neighbor in head.neighbors:
                if neighbor not in oldNodesToNew:
                    neighborCopy = Node(neighbor.val, [])
                    oldNodesToNew[head].neighbors.append(neighborCopy)
                    oldNodesToNew[neighbor] = neighborCopy
                    q.append(neighbor)
                else:
                    oldNodesToNew[head].neighbors.append(oldNodesToNew[neighbor])

        return res
    
    

# 40ms. 95th percentile. dfs recursive.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldNodesToNew = {}
        nodeCopy = Node(node.val, [])
        oldNodesToNew[node] = nodeCopy
        self.dfs(node, oldNodesToNew)
        return nodeCopy
        
        
    def dfs(self, node, oldNodesToNew):
        for neighbor in node.neighbors:
            if neighbor not in oldNodesToNew:
                neighborCopy = Node(neighbor.val, [])
                oldNodesToNew[node].neighbors.append(neighborCopy)
                oldNodesToNew[neighbor] = neighborCopy
                self.dfs(neighbor, oldNodesToNew)
            else:
                oldNodesToNew[node].neighbors.append(oldNodesToNew[neighbor])


"""
Notes:

They key here is to be able to pair old nodes with new ones. The search method doesn't really matte as long
as it traverses all the nodes.
"""