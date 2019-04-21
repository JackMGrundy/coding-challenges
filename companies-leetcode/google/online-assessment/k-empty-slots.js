/*
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
*/
// 1st attempt: 75th percentile in speed
/**
 * @param {number[]} flowers
 * @param {number} k
 * @return {number}
 */
var kEmptySlots = function(flowers, k) {
    var bloomed = new Set();
    
    var check = function(start, end) {
        if (start < 1 || end > flowers.length) return false;
        if (!bloomed.has(start) || !bloomed.has(end)) return false;
        for (let i = start+1; i < end; i++) {
            if (bloomed.has(i)) return false;
        }
        return true;
    }
    
    for (const [day, flower] of flowers.entries()) {
        bloomed.add(flower);
        if ( check(flower, flower+k+1) || check(flower-k-1, flower) ) return day+1;
    }
    return -1
};


// 2nd attempt: 85th percentile in speed
// Looks like entries() is slower...124ms for attempt 1 vs 112 for attempt 2. ~10% speedup
/**
 * @param {number[]} flowers
 * @param {number} k
 * @return {number}
 */
var kEmptySlots = function(flowers, k) {
    var bloomed = new Set();
    
    var check = function(start, end) {
        if (start < 1 || end > flowers.length) return false;
        if (!bloomed.has(start) || !bloomed.has(end)) return false;
        for (let i = start+1; i < end; i++) {
            if (bloomed.has(i)) return false;
        }
        return true;
    }
    
    for (let day = 0; day < flowers.length; day++) {
        let flower = flowers[day];
        bloomed.add(flower);
        if ( check(flower, flower+k+1) || check(flower-k-1, flower) ) return day+1;
    }
    return -1
};