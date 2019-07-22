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

// Attempt 1: 84ms, 50th percentile in speed
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
    
    links.forEach( link => {
        let a = link[0];
        let b = link[1];
        adjacencyList[a] = adjacencyList[a].concat(b);
    });
    
    return adjacencyList;
};


// Attempt 2: 64ms, 92nd percentile in speed
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