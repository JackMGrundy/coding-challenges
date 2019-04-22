/*
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
*/ 
// 44th percentile in speed:
import java.util.ArrayList;
import java.util.TreeSet;
class Solution {
    public String nextClosestTime(String time) {
        String [] components = time.split(":");
        String hours = components[0];
        String minutes = components[1];
        String [] nums = time.replace(":", "").split("");
        
        // Get all pairs of nums
        TreeSet<String> uniquePairs = new TreeSet<String>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                uniquePairs.add(nums[i] + nums[j]);
            }
        }
        ArrayList<String> pairs = new ArrayList<String> (uniquePairs);
        
        // Check if next minute is valid
        int i = pairs.indexOf(minutes);
        if (i+1 < pairs.size()) {
            int nxt = Integer.parseInt(pairs.get(i+1));
            if (nxt < 60 && nxt > 0) {
                return hours + ":" + pairs.get(i+1);
            }
        }
        
        // Check if next hour is valid
        i = pairs.indexOf(hours);
        if (i+1 < pairs.size()) {
            int nxt = Integer.parseInt(pairs.get(i+1));
            if (nxt < 24 && nxt > 0) {
                return pairs.get(i+1) + ":" + pairs.get(0);
            }
        }

        return pairs.get(0) + ":" + pairs.get(0);
        
    }
}