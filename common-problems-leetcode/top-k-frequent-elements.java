/* 
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
Accepted
195.4K
Submissions
359.2K
*/
// 93rd percentile. 11ms
/*
Bucket sort.
Count up the frequencies of the elements. Make a list of buckets of length
equal to the number of elements+1. The index of a bucket indicates frequency.
Therefore, the bucket list must be long enough to hold any frequency count because
at most a value can appear nums.length times. Stores all the nums in buckets according to 
their frequencies. Then iterate backwards over the buckets selecting out the most 
common elements. 
*/
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
        
        for(int num : nums) {
            counts.put(num, counts.getOrDefault(num, 0)+1);
        }
        
        List[] buckets = new List[nums.length+1];
        
        for(int num : counts.keySet() ) {
            int freq = counts.get(num);
            if (buckets[freq]==null) {
                buckets[freq] = new ArrayList<Integer>();
            }
            buckets[freq].add(num);
        }
        
        List<Integer> res = new ArrayList<Integer>();
        
        for (int i = nums.length; i >= 0; i--) {
            if (buckets[i] != null) {
                res.addAll(buckets[i]);
            }
            if (res.size() >= k) break;
        }
        
        while (res.size() > k) {
            res.remove(res.size()-1);
        }
        
        return res;
    }
}