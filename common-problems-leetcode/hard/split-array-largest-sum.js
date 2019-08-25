/*
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
*/

// DP method. O(m * (nums.length)^2)
// 156ms. 18th percentile. 
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number}
 */
var splitArray = function(nums, m) {
    const dp = Array.from( {length:nums.length+1}, () => 
                     Array.from( {length:m+1}, () => Infinity));
    
    const subSums = nums.reduce( (a,b,i) => {
        a.push(a[i]+b);
        return a;
    }, [0]);
    
    dp[0][0] = 0;
    for (let i = 1; i < nums.length+1; i++) {
        for (let j = 1; j < m+1; j++) {
            for (let k = 0; k < i; k++) {
                dp[i][j] = Math.min(dp[i][j], Math.max(subSums[i]-subSums[k], dp[k][j-1]));
            }
        }
    }
    return dp[nums.length][m];
};



// O(Nlog(sum of nums))
// 52ms. 89th percentile. boom. 
// love reduce so much. 
/**
 * @param {number[]} nums
 * @param {number} m
 * @return {number}
 */
var splitArray = function(nums, m) {
    let l = Math.max(...nums);
    let r = nums.reduce( (a,b) => {
        return a+b;
    }, 0);
    let minValidSum = r;
    
    while (l <= r) {
        let s = Math.floor((l+r) / 2.0);
        
        if (sumIsValid(nums, s, m)) {
            minValidSum = Math.min(minValidSum, s);
            r = s-1;
        } else {
            l = s+1;
        }
    }
    return minValidSum;
    
};

var sumIsValid = function(nums, s, m) {
    let currentTotal = 0;
    for (let num of nums) {
        if (currentTotal + num <= s) {
            currentTotal += num;
        } else {
            currentTotal = num;
            m -= 1;
            if (m === 0) {
                return false;
            }
        }
    }
    return true;
}