/*

There are a total of n courses you have to take, labeled from 0 to n-1.         

Some  courses  may  have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]                        

Given  the  total number of courses and a list of prerequisite pairs, return the
ordering of courses you should take to finish all courses.                      

There may be multiple correct orders, you just need to return one of them. If it
is impossible to finish all courses, return an empty array.                     

Example 1:                                                                      

Input: 2, [[1,0]]                                                               

Output: [0,1]                                                                   

Explanation: There are a total of 2 courses to take. To take course 1 you should
have finished                                                                   

             course 0. So the correct course order is [0,1] .                   

Example 2:                                                                      

Input: 4, [[1,0],[2,0],[3,1],[3,2]]                                             

Output: [0,1,2,3] or [0,2,1,3]                                                  

Explanation: There are a total of 4 courses to take. To take course 3 you should
have finished both                                                              

                 courses 1 and 2. Both courses 1 and 2 should be taken after you
finished course 0.                                                              

              So one correct course order is [0,1,2,3]. Another correct ordering
is [0,2,1,3] .                                                                  

Note:                                                                           

The input prerequisites is a graph represented by a list of edges, not adjacency
matrices. Read more about how a graph is represented.                           

You may assume that there are no duplicate edges in the input prerequisites.    


*/

// 4ms. 81 percentile.
class Solution {

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] degrees = new int[numCourses];
        Arrays.fill(degrees, 0);
        
        List<List<Integer>> leadsTo = new ArrayList<>();
        for (int course = 0; course < numCourses; course++) {
            leadsTo.add(new ArrayList<Integer>());
        }
        
        for (int[] pair : prerequisites) {
            Integer course = pair[0];
            Integer prerequisite = pair[1];
            leadsTo.get(prerequisite).add(course);
            degrees[course]++;
        }
        
        Queue<Integer> q = new LinkedList<>();
        for (int course = 0; course < numCourses; course++) {
            if (degrees[course] == 0) {
                q.add(course);
            }
        }

        int[] result = new int[numCourses];
        int coursesAccountedFor = 0;
        
        while (0 < q.size()) {
            int cur = q.remove();
            result[coursesAccountedFor] = cur;
            coursesAccountedFor++;

            for (int neighbor : leadsTo.get(cur)) {
                if (0 < degrees[neighbor]) {
                    degrees[neighbor]--;
                    if (degrees[neighbor] == 0) {
                        q.add(neighbor);
                    }
                }
            }
        }
        return coursesAccountedFor == numCourses ? result : new int[0];
    }
}

/*

Notes:

Straight topological sort problem (see notes in algos folder)

For optimizing the implementation, it's typical Java...I first implemented
this with hashmaps for the degrees and leadsTo mappings, but you can
get a 2x speedup on these test cases using lists and arrays instead.

*/