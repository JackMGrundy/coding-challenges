/*
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
*/

// 88ms. 43 percentile.
// No time to speedup...If there were time...I'd do the counting and mod parts simultaneously...
/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var subarraysDivByK = function(A, K) {
    let cumSum = A.reduce( (a,b,i) => {
        let temp = (a[i]+b)%K;
        if (temp < 0) {
            temp += K;
        }
        a.push( temp );
        return a;
    }, [0]);
    
    let remainderCounts = cumSum.reduce( (a,b) => {
        a[b] = b in a ? a[b]+1 : 1;
        return a;
    }, {});
    
    let res = 0;
    for (let key in remainderCounts) {
        let count = remainderCounts[key];
        res += Math.floor(count*(count-1)/2);
    }
    return res;
};



/*
anoying that java/javascript can return negative mods...note adding K fixes it
*/