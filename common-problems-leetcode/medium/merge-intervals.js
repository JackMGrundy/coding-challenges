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
// 1st attempt: 97th percentile
/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    if (intervals.length===0) return [];
    intervals.sort( (a, b) => a.start - b.start);
    s = [ intervals[0] ];
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i].start <= s[s.length-1].end) {
            s[s.length-1].end = Math.max(s[s.length-1].end, intervals[i].end);
        } else {
            s.push(intervals[i]);
        }
    }
    return s;
};