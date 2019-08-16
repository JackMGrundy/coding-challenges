/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
*/

// 1st attempt: 77th percentile in speed. 2 passes approach
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    if (height.length==0) return 0;
    let guesses = new Array(height.length)
    let peak = 0;
    
    for (let i = 0; i < height.length; i ++) {
        guesses[i] = Math.max(peak-height[i], 0)
        peak = Math.max(peak, height[i])
    }
    peak = 0
    for (i = height.length-1; i >= 0; i--) {
        guesses[i] = Math.min( Math.max(peak-height[i], 0), guesses[i] )
        peak = Math.max(peak, height[i])
    }
    return guesses.reduce( (partialSum, a) => partialSum+a )
};


// 2nd attempt: 89th percentile in speed. Pincer approach.
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let res = 0,
        l = 0,
        r = height.length-1;
    let lMax = height[l],
        rMax = height[r];
    
    while (l < r) {
        lMax = Math.max(lMax, height[l]);
        rMax = Math.max(rMax, height[r]);
        
        if (lMax <= rMax) {
            res += lMax - height[l];
            l += 1;
        } else {
            res += rMax - height[r];
            r -= 1;
        }
    }
    return res;
};