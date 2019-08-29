/*
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
*/

// 5ms. 26th percentile.
// Looks like this is as good as it gets for a bfs solution. DFS can get you to 4ms. 
// Union find solutions are the 70+ percentile solutions. 
class Solution {
    public int findCircleNum(int[][] M) {
        if (M.length < 2) {
            return M.length;
        }
        int groups = 0;
        int numPeople = M[0].length;
        Set<Integer> seen = new HashSet<Integer>();
        
        for (int person = 0; person < numPeople; person++) {
            if (!seen.contains(person)) {
                groups++;
                Queue<Integer> q = new LinkedList<Integer>();
                q.add(person);
                while(q.size() > 0) {
                    int friend = q.remove();
                    if (seen.contains(friend)) {
                        continue;
                    } else {
                        seen.add(friend);
                        for (int nextFriend = 0; nextFriend < numPeople; nextFriend++) {
                            boolean connected = (M[friend][nextFriend] == 1);
                            if (connected && !seen.contains(nextFriend)) {
                                q.add(nextFriend);
                            }
                        }
                    }
                }
            }
        }
        
        return groups;
    }
}