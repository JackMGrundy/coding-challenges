/*
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted
24,452
Submissions
57,249
*/

// 100th percentile. 196ms.
/**
 * @param {number[]} w
 */
var Solution = function(w) {
    let totalWeight = w.reduce( (a,b) => a+b );
    let cumulativeSum = 0;
    this.indexCutoffs = [];
    w.forEach(weight => {
        cumulativeSum += parseFloat(weight)/totalWeight;
        this.indexCutoffs.push(cumulativeSum);
    })
};

/**
 * @return {number}
 */
Solution.prototype.pickIndex = function() {
    let target = Math.random();
    let l = 0, r = this.indexCutoffs.length-1;
    while (l < r) {
        let mid = Math.floor((l+r)/2);
        if ( target > this.indexCutoffs[mid] ) {
            l = mid+1;
        } else {
            r = mid;
        }
    }
    return l;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(w)
 * var param_1 = obj.pickIndex()
 */