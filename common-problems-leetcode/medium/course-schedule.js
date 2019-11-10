/*
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
*/

// 64ms, 92nd percentile in speed
// ES6 for of loops appear much faster than forEach loops
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let adjacencyList = getAdjacencyList(numCourses, prerequisites);
    
    let visited = Array(numCourses).fill(false);
    let recStack = Array(numCourses).fill(false);
    
    for (let course = 0; course < numCourses; course++) {
        if (visited[course] === false) {
            if (detectCycle(course, adjacencyList, recStack, visited) === true) {
                return false;
            }
        }
    }
    
    return true;
};

let detectCycle = function(node, adjacencyList, recStack, visited) {
    recStack[node] = true;
    visited[node] = true;
    
    for (const neighbor of adjacencyList[node]) {
        if (recStack[neighbor] === true) {
            return true;
        }
        if (visited[neighbor] === false) {
            if ( detectCycle(neighbor, adjacencyList, recStack, visited)) {
                return true;
            }
        }
    }
    
    recStack[node] = false;
    return false;
};

let getAdjacencyList = function(numNodes, links) {
    let adjacencyList = {};
    for (let node = 0; node < numNodes; node++) {
        adjacencyList[node] = Array();
    }
    
    for (const link of links) {
        let a = link[0];
        let b = link[1];
        adjacencyList[a] = adjacencyList[a].concat(b);
    }
    
    return adjacencyList;
};



/*

Notes:


See notes on cycle detection

DFS approach:
Convert links to a graph where given a node, you can get a list of neighbors.
For each node, check if there is a cycle. Only check if it hasn't already
been ok'ed (visited)

To check for a cycle:
    Given that the nodes are 0 to N-1, we keep a simple N length list to
    record nodes in the call stack.

    We keep a similar list called "visited" to note the nodes we have
    already ok'ed. 

    We start the dfs on a given node. We note it as both visited and in
    the call stack.

    We use the graph to iterate through its neighbors. If we see a neighbor
    that is already in the stack, we found a cycle.

    Otherwise, if the neighbor hasn't been visited, we make a recursive call
    that starts at that node. This recursive call will continue the path. Via the
    the rec stack list, it will remember that that the previous node is in
    the rec stack.

    Finally, back in the first call in the recursion stack, we mark that
    this node is no longer in the recursion stack and return that there isn't 
    a cycle. We only get here if a cycle wasn't found at either this level
    or at a deeper level in the recursion stack.


Intuition for visited:
Say we pass through node A while processing a path. We found no cycle on this
path. Because we recorded A as visited, we won't visit it again, either as
the start of a path or as part of another path. 

This is ok. As part of the already traversed path, we already examined all outgoing
edges from A. Therefore, if we started a different path that went through A,
we would end up just traversing those same outlinks again and again find that there
is no cycle. 


*/