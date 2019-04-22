/*
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
*/
// 100th percentile in speed
/**
 * @param {string} time
 * @return {string}
 */
var nextClosestTime = function(time) {
    let nums = time.replace(':','').split('');
    time = time.split(":");
    let hours = time[0],
        minutes = time[1];
    let pairs = [];
    
    // Construct all possible pairs of numbers
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            pairs.push(nums[i]+nums[j]);
        }
    }
    // Make sure pairs are unique and sorted ascending
    pairs.sort()
    pairs = [...new Set(pairs)];
    
    // Check if next time (in terms of mins) is valid
    let i = pairs.indexOf(minutes);
    if (i+1 < pairs.length && pairs[i+1] < "60") {
        return hours + ":" + pairs[i+1];
    }
    // Check if next time (in terms of hours) is valid
    i = pairs.indexOf(hours);
    if (i+1 < pairs.length && pairs[i+1] < "24") {
        return pairs[i+1] + ":" + pairs[0];
    }
    // Return the first time the next day
    // The first pair must be less than 24...otherwise
    // the original time could not have been valid
    return pairs[0] + ":" + pairs[0];
};