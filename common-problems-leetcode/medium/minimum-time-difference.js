/* 
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
*/


// 56ms. 98th percentile.
/**
 * @param {string[]} timePoints
 * @return {number}
 */
var findMinDifference = function(timePoints) {
    let memo = Array(24*60).fill(0);
    
    for (let timePoint of timePoints) {
        let hours = parseInt(timePoint.slice(0, 2));
        let minutes = parseInt(timePoint.slice(3, 5));
        let totalMinutes = hours*60 + minutes;
        memo[totalMinutes]++;
        
        if (memo[totalMinutes] > 1) {
            return 0;
        }
    }
    
    let first = 24*60+1;
    let last = -24*60-1;
    let best = Infinity;
    for (let i = 0; i < memo.length; i++) {
        if (memo[i] === 1) {
            best = Math.min(best, i-last);
            first = Math.min(first, i);
            last = Math.max(last, i);
        } 
    }
    
    best = Math.min(best, 24*60+first-last);
    return best;
};