/*
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
*/
// 1ms. 38th percentile. 
class Solution {
    public int firstMissingPositive(int[] nums) {
        if (nums.length == 0) {
            return 1;
        }
        int[] numsWithZero = new int[nums.length+1];
        for (int i = 0; i < nums.length; i++) {
            numsWithZero[i+1] = nums[i];
        }
        
        int minPositiveValue = Integer.MAX_VALUE;
        for (int i = 0; i < numsWithZero.length; i++) {
            if (numsWithZero[i] < minPositiveValue) {
                minPositiveValue = numsWithZero[i];
            }
        }
        
        if (minPositiveValue > 1) {
            return 1;
        }
        
        for (int i = 0; i < numsWithZero.length; i++) {
            int num = numsWithZero[i];
            if (num < 0) {
                continue;
            }
            else if (num == i) {
                continue;
            }
            else if (0 < num && num < numsWithZero.length) {
                numsWithZero[i] = -1;
                while (0 < num && num < numsWithZero.length) {
                    if (numsWithZero[num] == num) {
                        break;
                    }
                    int temp = numsWithZero[num];
                    numsWithZero[num] = num;
                    num = temp;
                }
            }
        }
        
        for (int i = 1; i < numsWithZero.length; i++) {
            if (numsWithZero[i] != i) {
                return i;
            }
        }
        
        return numsWithZero.length;
    }
}