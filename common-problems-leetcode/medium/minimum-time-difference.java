/* 
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
*/

// 11ms. 54th percentile. O(Nlog(N))
// Wow...surprised this is an ok solution. I assumed this would be crap compared to whatever O(N)
// trick there surely is.
class Solution {
    public int findMinDifference(List<String> timePoints) {
        Collections.sort(timePoints);

        int prevHours = Integer.parseInt(timePoints.get(0).substring(0, 2));
        int prevMinutes = Integer.parseInt(timePoints.get(0).substring(3, 5));
        int prevTotalMins = 60*prevHours + prevMinutes;
        
        int finalHours = Integer.parseInt(timePoints.get(timePoints.size()-1).substring(0, 2));
        int finalMins = Integer.parseInt(timePoints.get(timePoints.size()-1).substring(3, 5));
        int finalTime = 60*finalHours + finalMins;
        
        int best = (24*60+prevTotalMins) - finalTime;
        
        for (int i = 1; i < timePoints.size(); i++) {
            int curHours = Integer.parseInt(timePoints.get(i).substring(0, 2));
            int curMinutes = Integer.parseInt(timePoints.get(i).substring(3, 5));
            int curTotalMins = 60*curHours + curMinutes;
            
            best = Math.min(best, curTotalMins - prevTotalMins);
            prevTotalMins = curTotalMins;
        }
        
        
        
        return best;
    }
}



// 2ms. 99th percentile.
// Just make a bucket for every minute, fill accordingly. Make sure to check the first vs the last.
class Solution {
    public int findMinDifference(List<String> timePoints) {
        int[] memo = new int[24*60];
        
        for (int i = 0; i < timePoints.size(); i++) {
            int hours = Integer.parseInt(timePoints.get(i).substring(0, 2));
            int minutes = Integer.parseInt(timePoints.get(i).substring(3, 5));
            int totalMinutes = 60*hours + minutes;
            memo[totalMinutes]++;
            
            if (memo[totalMinutes] > 1) {
                return 0;
            }
        }
        
        int first = 24*60+1;
        int last = -24*60+1;
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < memo.length; i++) {
            if (memo[i] == 1) {
                best = Math.min(best, i-last);
                first = Math.min(first, i);
                last = Math.max(last, i);
            }
        }
        best = Math.min(best, 24*60+first - last);
        
        return best;
    }
}