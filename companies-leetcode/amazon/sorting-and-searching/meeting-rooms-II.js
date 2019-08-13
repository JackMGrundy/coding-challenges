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

// 1st attempt. 80ms. 62nd percentile
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {
    if (intervals === null || intervals.length === 0) {
        return 0;
    }
    
    let starts = new Array(intervals.length);
    let ends = new Array(intervals.length);
    for (let i = 0; i < intervals.length; i++) {
        starts[i] = intervals[i][0];
        ends[i] = intervals[i][1];
    }
    
    starts.sort( (a,b) => a-b);
    ends.sort( (a,b) => a-b);
    
    let startsPointer = 0;
    let endsPointer = 0;
    let maxNumOverlappingMeetings = 0;
    let curNumOverlappingMeetings = 0;
    
    while (startsPointer < starts.length) {
        
        while (startsPointer < starts.length && starts[startsPointer] < ends[endsPointer]) {
            curNumOverlappingMeetings++;
            startsPointer++;
        }
        
        maxNumOverlappingMeetings = Math.max(maxNumOverlappingMeetings, curNumOverlappingMeetings);
        
        while (startsPointer < starts.length && starts[startsPointer] >= ends[endsPointer]) {
            curNumOverlappingMeetings--;
            endsPointer++;
        }
    }
    
    return maxNumOverlappingMeetings;
};





// 2nd attempt. 76ms. 75th percentile.
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {
    let starts = new Array(intervals.length);
    let ends = new Array(intervals.length);
    for (let i = 0; i < intervals.length; i++) {
        starts[i] = intervals[i][0];
        ends[i] = intervals[i][1];
    }
    
    starts.sort( (a,b) => a-b);
    ends.sort( (a,b) => a-b);
    
    let startsPointer = 0;
    let endsPointer = 0;
    let maxNumOverlappingMeetings = 0;
    let curNumOverlappingMeetings = 0;
    
    while (startsPointer < starts.length) {
        
        while (startsPointer < starts.length && starts[startsPointer] < ends[endsPointer]) {
            curNumOverlappingMeetings++;
            startsPointer++;
        }
        
        maxNumOverlappingMeetings = Math.max(maxNumOverlappingMeetings, curNumOverlappingMeetings);
        
        while (startsPointer < starts.length && starts[startsPointer] >= ends[endsPointer]) {
            curNumOverlappingMeetings--;
            endsPointer++;
        }
    }
    
    return maxNumOverlappingMeetings;
};







// 3rd attempt: 72ms. 88th percentile.
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minMeetingRooms = function(intervals) {
    let starts = [];
    let ends = [];
    for (let i = 0; i < intervals.length; i++) {
        starts[i] = intervals[i][0];
        ends[i] = intervals[i][1];
    }
    
    starts.sort( (a,b) => a-b);
    ends.sort( (a,b) => a-b);
    
    let startsPointer = 0;
    let endsPointer = 0;
    let maxNumOverlappingMeetings = 0;
    let curNumOverlappingMeetings = 0;
    
    while (startsPointer < starts.length) {
        
        while (startsPointer < starts.length && starts[startsPointer] < ends[endsPointer]) {
            curNumOverlappingMeetings++;
            startsPointer++;
        }
        
        maxNumOverlappingMeetings = Math.max(maxNumOverlappingMeetings, curNumOverlappingMeetings);
        
        while (starts[startsPointer] >= ends[endsPointer]) {
            curNumOverlappingMeetings--;
            endsPointer++;
        }
    }
    
    return maxNumOverlappingMeetings;
};