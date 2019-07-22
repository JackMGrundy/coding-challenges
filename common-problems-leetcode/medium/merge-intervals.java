/*
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Accepted
324,573
Submissions
921,724
*/
// 1st attempt: 37ms. 35th percentile. Solutions fall into two groups clustered around 37ms and 7ms. The 7ms solutions
// are substantially more complex / harder to reader. I'd opt for the extra readability. 
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
    
        List<int[]> res = new ArrayList<>();

        int[] cur = intervals[0];
        res.add(cur);
        
        for (int i = 1; i < intervals.length; i++) {
            if ( intervals[i][0] <= cur[1] ) {
                cur[1] = Math.max(cur[1], intervals[i][1]);
            } else {
                cur = intervals[i];
                res.add(cur);
            }
        }
        
        return res.toArray(new int[res.size()][]);
    }
}