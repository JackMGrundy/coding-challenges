/*
Given an undirected graph, return true if and only if it is bipartite.          

Recall  that  a  graph  is  bipartite if we can split it's set of nodes into two
independent  subsets A and B such that every edge in the graph has one node in A
and another node in B.                                                          

The  graph  is  given in the following form: graph[i] is a list of indexes j for
which  the edge between nodes i and j exists.  Each node is an integer between 0
and  graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.                        

Example 1:                                                                      

Input: [[1,3], [0,2], [1,3], [0,2]]                                             

Output: true                                                                    

Explanation:                                                                    

The graph looks like this:                                                      

0----1                                                                          

|    |                                                                          

|    |                                                                          

3----2                                                                          

We can divide the vertices into two groups: {0, 2} and {1, 3}.                  

Example 2:                                                                      

Input: [[1,2,3], [0,2], [0,1,3], [0,2]]                                         

Output: false                                                                   

Explanation:                                                                    

The graph looks like this:                                                      

0----1                                                                          

| \  |                                                                          

|  \ |                                                                          

3----2                                                                          

We cannot find a way to divide the set of nodes into two independent subsets.   

                                                                                

Note:                                                                           

graph will have length in range [1, 100].                                       

graph[i] will contain integers in range [0, graph.length - 1].                  

graph[i] will not contain i or duplicate values.                                

The  graph  is  undirected:  if  any element j is in graph[i], then i will be in
graph[j].                                                                       

*/

// 1ms. 66 percentile.
// Iterative.
import java.util.Stack;
class Solution {
    public boolean isBipartite(int[][] graph) {
        int numberOfVertices = graph.length;
        boolean[] assigned = new boolean[numberOfVertices];
        int[] assignments = new int[numberOfVertices];
        Stack<Integer> stack = new Stack<>();
        
        for (int vertex = 0; vertex < numberOfVertices; vertex++) {
            if (!assigned[vertex]) {
                assigned[vertex] = true;
                assignments[vertex] = 1;
                stack.push(vertex);
                
                while (0 < stack.size()) {
                    int root = stack.pop();
                    for (int neighbor : graph[root]) {
                        if (!assigned[neighbor]) {
                            assignments[neighbor] = assignments[root]*-1;
                            assigned[neighbor] = true;
                            stack.push(neighbor);
                        } else if (assignments[neighbor] == assignments[root]) {
                            return false;
                        }
                    }
                }
            }
        }
        
        return true;
    }
}



// 0ms. 100th percentile.
// recursive
class Solution {
    public boolean isBipartite(int[][] graph) {
        int[] assignments = new int[graph.length];
        
        for (int i = 0; i < graph.length; i++) {
            if (assignments[i] == 0 && !isValid(graph, assignments, i, 1)) {
                return false;
            }
        }
        
        return true;
    }
    
    boolean isValid(int[][] graph, int[] assignments, int node, int expectedAssignment) {
        if (assignments[node] != 0) {
            return assignments[node] == expectedAssignment;
        }
        
        assignments[node] = expectedAssignment;
        
        for (int neighbor : graph[node]) {
            if (!isValid(graph, assignments, neighbor, expectedAssignment == 1 ? 2 : 1)) {
                return false;
            }
        }
        
        return true;
    }
}


/*
Notes:

Brute force would be to try all combinations. This is prohibitive. It would be (2^N)

We can solve this with dfs. We put the first node we see in one group...then as we dfs
our way through the other nodes we keep flipping the group...lets say we come across
a node that's already been assigned a group and that it's different from what we want
to assign it, then we don't have a matching that works. 

Note the first for loop:
    We need this because of cases like:
    o ----------- o
    o ----------- o
    o ----------- o
    In this case each dfs just hops us along one link


JAVA SPECIFIC NOTES:
This brings up an interesting thought about autoboxing. With an iterative solution,
you get stuck with switching back and forth between Integer and int because Stack
requires generic tying. Hence annoying autoboxing.

With a recursive solution you avoid the generics and everything remains in primitive land. 
*/