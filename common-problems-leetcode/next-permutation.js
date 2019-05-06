/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Accepted
231.5K
Submissions
762K
*/
// 100th percentile. 68ms.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    
    if (nums.length <= 1) {}
    
    // check if max permutation already
    sortedDesc = true;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i-1]<nums[i]) {
            sortedDesc = false;
            break;
        }
    }
    if (sortedDesc) {
        nums.sort( (a, b) => a-b);
    } else {
        let pivotIndex = nums.length - 2;
        while (pivotIndex >= 0) {
            let pivot = nums[pivotIndex];
            let minItem = Number.MAX_SAFE_INTEGER;
            let minIndex = -1;
            // Is there an item to the right of pivot less than pivot
            for (let i = pivotIndex+1; i < nums.length; i++) {
                if (nums[i] > pivot && nums[i] < minItem) {
                    minItem = nums[i];
                    minIndex = i;
                }
            }
            // swap pivot with the smallest item to the right that is greater than pivot
            if (minItem < Number.MAX_SAFE_INTEGER && minItem > pivot) {
                nums[pivotIndex] = minItem;
                nums[minIndex] = pivot;
                let sl = nums.slice(pivotIndex+1, nums.length).sort((a,b) => a-b);
                nums.splice(pivotIndex+1, nums.length, ...sl);
                break
            }   
            else {
                pivotIndex--;
            }
        }
    }  
};