/*
Given  an  array  nums containing n + 1 integers where each integer is between 1
and  n  (inclusive), prove that at least one duplicate number must exist. Assume
that there is only one duplicate number, find the duplicate one.                

Example 1:                                                                      

Input: [1,3,4,2,2]                                                              

Output: 2                                                                       

Example 2:                                                                      

Input: [3,1,3,4,2]                                                              

Output: 3                                                                       

Note:                                                                           

You must not modify the array (assume the array is read only).                  

You must use only constant, O(1) extra space.                                   

Your runtime complexity should be less than O(n2).                              

There  is  only one duplicate number in the array, but it could be repeated more
than once.                                                                      

*/
// 56ms. 81 percentile.
// Fun use of do while instead of plain while (also works)
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let slow = 0, fast = 0;
    
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (fast != slow);
    fast = 0;
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
};

/*

Notes:

The simple solutions to this problem are not very interesting.
The constant space solution is interesting.

Basically it's a straightup implementation of Floyd's Tortoise and Hare
cycle detection algo. See notes on this algo for details. 

*/