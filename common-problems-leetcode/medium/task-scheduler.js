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
// 87th percentile 108ms
/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    let counts = new Map();
    tasks.forEach(task => {
        counts.set(task, counts.get(task)+1 || 1);
    });

    let maxCount = 0;
    let numMaxCount = 0;
    counts.forEach( (count, key) => {
        if (count > maxCount) {
            numMaxCount = 1;
            maxCount = count;
        } else if (count === maxCount) {
            numMaxCount++;
        }
    })

    return Math.max(tasks.length, (n+1)*(maxCount-1)+numMaxCount);
};