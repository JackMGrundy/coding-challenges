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

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) 
    {
        //topo sort
       // hm key is subj, value is list of all to tkae before, initialized with itself
        //go through value, start with itself and go to next, backtracking in hashmap
        //or set of  degrees and neighbors
        List[] course=new List[numCourses];
        int[] map=new int[numCourses];
        List<Integer> ans=new ArrayList<Integer>();
        for(int i=0;i<numCourses;i++)
            course[i]=new ArrayList<Integer>();
        for(int i=0;i<prerequisites.length;i++)
            course[prerequisites[i][0]].add(prerequisites[i][1]);
        for(int i=0;i<numCourses;i++)
            if(dfs(course,i,ans,map)==false) return new int[0];
            int[] an=new int[ans.size()];
        for(int i=0;i<ans.size();i++)
            an[i]=ans.get(i);
        return an;
    }
    public boolean dfs(List[] course,int req,List<Integer> ans,int[] map)
    {
        if(map[req]==0)
        {
            map[req]=1;
            for(int i=0;i<course[req].size();i++) 
                if(dfs(course,(int)course[req].get(i),ans,map)==false) return false;
            map[req]=2;
        } 
        else if(map[req]==1) return false;
        else if(map[req]==2) return true;
        ans.add(req);
        return true;
    }
}







class Solution {
    private static int[] visited;
     private static List[] edges;
     private static List<Integer> sortedlist;
 
     public int[] findOrder(int numCourses, int[][] prerequisites) {
         if(numCourses == 0){
             return new int[numCourses];
         }
         if(prerequisites == null || prerequisites.length == 0 || prerequisites[0] == null || prerequisites[0].length == 0){
             int [] res = new int[numCourses];
             for(int i = 0;i < numCourses; i ++){
                 res[i] = i;
             }
             return res;
         }
         visited = new int[numCourses];
         edges = new List[numCourses];
         sortedlist = new ArrayList<>();
         for(int i = 0; i < numCourses; i ++){
             edges[i] = new ArrayList<>();
         }
         for(int[] prerequisite : prerequisites){
             edges[prerequisite[1]].add(prerequisite[0]);
         }
         for(int i = 0;i < numCourses; i ++){
             if(!dfs(i)){
                 return new int[0];
             }
         }
         int[] res = new int[numCourses];
         for(int i = 0;i < numCourses;i ++){
             res[i] = sortedlist.get(i);
         }
         return res;
     }
     public boolean dfs(int node){
         if(visited[node] == 1){
             return true;
         }
         else if(visited[node] == -1){
             return false;
         }
         visited[node] = -1;
         List<Integer> list = edges[node];
         for(int li : list){
             if(!dfs(li)){
                 return false;
             }
         }
         visited[node] = 1;
         sortedlist.add(0 , node);
         return true;
     }
 }

/*

Notes:


*/