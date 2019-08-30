/*
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3] 
*/

// 92ms. 94th percentile.
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let res = [];
    
    for (let num of nums) {
        let index = Math.abs(num)-1;
        if (nums[index] < 0) {
            res.push(index+1);
        } else {
            nums[index] *= -1;
        }
    }
    return res;
};




/*
Notes:
First impulse is to make a messy swap solution like the first one.
The key thing to note though is that we just want to use an array element to hold two pieces of info
1) have we already seen a value of that index
2) the actual number there

The swapping business is try to sort out the actual number there so that we can store "we have seen the value
of this index".

The smarter solution is to just make the element store both. The absolute value of the number there holds
2) and whether or not it's negative holds 1). 
*/