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
// 99th percentile. 1ms.
import java.util.Arrays;
class Solution {
    public void nextPermutation(int[] nums) {
        
        if (nums.length <= 1) {
            ;
        }
        else {
            // check if max perm
            boolean sortedDesc = true;
            for (int i = 1; i < nums.length; i++) {
                if (nums[i-1] < nums[i]) {
                    sortedDesc = false;
                    break;
                }
            }
            // max perm...restart
            if(sortedDesc) {
                Arrays.sort(nums);
            } else {
                int pivotIndex = nums.length-2;
                while (pivotIndex >= 0) {
                    int pivot = nums[pivotIndex];
                    int minItem = Integer.MAX_VALUE;
                    int minIndex = -1;
                    // find minimum item to right of pivot
                    for (int i = pivotIndex+1; i < nums.length; i++) {
                        if (nums[i] > pivot && nums[i] < minItem) {
                            minItem = nums[i];
                            minIndex = i;
                        }
                    }
                    // there is an item to the right of pivot greater than it
                    if (minItem < Integer.MAX_VALUE && minItem > pivot) {
                        nums[minIndex] = pivot;
                        nums[pivotIndex] = minItem;
                        Arrays.sort(nums, pivotIndex+1, nums.length);
                        break;
                    } else {
                        pivotIndex--;
                    }
                }
            }
            
        }
    }
}