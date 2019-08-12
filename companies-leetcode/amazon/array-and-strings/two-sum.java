/*
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
*/

// 1st attempt. 2ms. 29th percentile
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] res = new int[2];
        if (numbers.length == 0) {
            return res;
        }
        HashMap<Integer, Integer> validPartners = new HashMap<Integer, Integer>();
        for (int i = 1; i <= numbers.length; i++) {
            if (validPartners.containsKey(numbers[i-1])) {
                res[0] = validPartners.get(numbers[i-1]);
                res[1] = i;
                return res;
            } else {
                validPartners.put(target-numbers[i-1], i);
            }
        }
        
        return res;
    }
}



// 2nd attempt. 1ms. 60th percentile
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;
        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                break;
            }
            else if (numbers[l] + numbers[r] < target) {
                l++;
            }
            else if (numbers[l] + numbers[r] > target) {
                r--;
            }
        }
        
        int[] res = {l+1, r+1};
        return res;
    }
}



// 3rd attempt. 0ms. 100th percentile
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;
        while (l < r) {
            if (numbers[l] + numbers[r] < target) {
                l++;
            }
            else if (numbers[l] + numbers[r] > target) {
                r--;
            }
            else {
                break;
            }
        }
        
        int[] res = {l+1, r+1};
        return res;
    }
}
