/*
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
Accepted
82,242
Submissions
181,812
*/
// 48th percentile 19ms
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> counts = new HashMap<Character, Integer>();
        for (int i = 0; i < tasks.length; i++) {
            counts.put(tasks[i], counts.getOrDefault(tasks[i], 0)+1);
        }
        
        int maxCount = 0;
        int numMaxCount = 0;
        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
            int nxt = entry.getValue();
            if (nxt == maxCount) {
                numMaxCount++;
            } else if (nxt > maxCount) {
                numMaxCount = 1;
                maxCount = nxt;
            }
        }
        
        return Math.max(tasks.length, (n+1)*(maxCount-1)+numMaxCount);
    }
}

// 100th percentile
//...don't forget the benefits of int arrays when working with chars
class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] counts = new int[26];
        for (char c : tasks){ 
            counts[c - 'A']++;
        }
        int maxCount = 0, numMaxCount = 0;
        for (Integer i : counts) {
            if (i == maxCount) {
                numMaxCount++;
            } else if (i > maxCount) {
                numMaxCount = 1;
                maxCount = i;
            }
        }
        
        return Math.max(tasks.length, (n+1)*(maxCount-1)+numMaxCount);
    }
}

