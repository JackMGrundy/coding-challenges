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

// Attempt 1: 5ms, 70th percentile in speed
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> neighborMap = this.getAdjacencyList(prerequisites, numCourses);
        
        boolean[] visited = new boolean[numCourses];
        boolean[] recStack = new boolean[numCourses];
        
        for (int course = 0; course < numCourses; course++) {
            if (!visited[course]) {
                if (this.detectCycle(course, neighborMap, visited, recStack)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    public boolean detectCycle(int course,  Map<Integer, ArrayList<Integer>> neighborMap, boolean[] visited, boolean[] recStack) {
        visited[course] = true;
        recStack[course] = true;
        
        ArrayList<Integer> neighbors = neighborMap.get(course);
        for(Integer neighbor : neighbors) {
            if (recStack[neighbor]) {
                return true;
            }
            else if (!visited[neighbor]) {
                if (this.detectCycle(neighbor, neighborMap, visited, recStack)) {
                    return true;
                }
            }
        }
        
        recStack[course] = false;
        return false;
    }
    
    
    public Map<Integer, ArrayList<Integer>> getAdjacencyList(int[][] prerequisites, int numCourses) {
        Map<Integer, ArrayList<Integer>> adjacencyList = new HashMap<Integer, ArrayList<Integer>>();
        
        for (int i = 0; i < numCourses; i++) {
            ArrayList<Integer> temp = new ArrayList<Integer>();
            adjacencyList.put(i, temp);
        }
        
        for (int i = 0; i < prerequisites.length; i++) {
            int course = prerequisites[i][0];
            int prerequisite = prerequisites[i][1];
            
            ArrayList<Integer> temp = adjacencyList.get(course);
            temp.add(prerequisite);
            adjacencyList.put(course, temp);
        }
        
        return adjacencyList;
    }
}