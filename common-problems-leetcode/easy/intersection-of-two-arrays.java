/*
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
*/
// 2ms. 98th percentile.
import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> s = new HashSet<Integer>();
        Set<Integer> matches = new HashSet<Integer>();
        for (int num : nums1) {
            s.add(num);
        }
        
        for (int num : nums2) {
            if (s.contains(num)) {
                matches.add(num);
            }
        }
        
        int[] res = new int[matches.size()];
        int i = 0;
        for (int num : matches) {
            res[i++] = num;
        }
        
        return res;
    }
}