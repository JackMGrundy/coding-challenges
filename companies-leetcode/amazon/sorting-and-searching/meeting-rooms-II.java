/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
*/

// 1st attempt. 2ms. 100th percentile
import java.util.*;
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return 0;
        }
        int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        
        Arrays.sort(starts);
        Arrays.sort(ends);
        
        int maxNumOverlappingMeetings = 0;
        int curNumOverlappingMeetings = 0;
        int startsPointer = 0;
        int endsPointer = 0;
        
        while (startsPointer < starts.length) {
            
            while (startsPointer < starts.length && starts[startsPointer] < ends[endsPointer]) {
                startsPointer++;
                curNumOverlappingMeetings++;
            }
            
            maxNumOverlappingMeetings = Math.max(maxNumOverlappingMeetings, curNumOverlappingMeetings);
            
            
            while (starts[startsPointer] >= ends[endsPointer]) {
                endsPointer++;
                curNumOverlappingMeetings--;
            }
        }
        
        
        return maxNumOverlappingMeetings;
    }
}