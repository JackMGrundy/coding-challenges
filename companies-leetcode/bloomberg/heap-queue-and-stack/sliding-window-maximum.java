/*
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
*/

/*
Cool problem. Here's intuition.
Maintain a deque. The deque will contain monotonically decreasing values. The head of the deque (left) will contain the max value. The deque will 
represent a subsequence of the array. 

To maintain it:
When moving increasing the range of the window, pop elements from the tail of the deque until you hit a value that is greater than the new value. Then
add the new value. 

When decreasing the range of the window, look at the value being removed. If it equals the head of the deque, pop the head of the deque. 

3 keys observations:
1) when we increase the range of the window, we observe a new value x. If this value is greater than values we have already seen and are 
still considering, then those old values could never be a max again because they will be dropped before this new greater value.

2) the operation to maintain the deque after increasing the window size is amortized constant time (emphasis). To see this, note that in the 
worst case the new value x observed by increasing the window size is greater than every value in the deque. In this case we have to do k pops. However, 
after this happens, the deque will just have x. In the worst case, the next time we increasing the window size we can only do a single pop. Let's
for the next k values we observe, we do no pops. Then we've constant work for these k elements. Now say we have to do k pops for the new element. 
Then we've ultimately done 2 operations (a push and a pop) for each the elements in the deque. 

3) The operation to maintain the deque after decreasing the window size is obviously constant time. 
*/

// 11ms. 58th percentile.
import java.util.*;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0 || k == 0) {
            return new int[0];
        }
        Deque<Integer> d = new LinkedList<Integer>();
        int[] maxes = new int[nums.length-k+1];

        for (int i = 0; i < nums.length; i++) {
            if (!d.isEmpty() && i-k >= 0 && nums[i-k] == d.peekFirst()) {
                d.removeFirst();
            }
            int newValue = nums[i];
            while (!d.isEmpty() && newValue > d.peekLast()) {
                d.removeLast();
            }
            d.add(newValue);
            
            if (i >= k-1) {
                maxes[i-k+1] = d.peekFirst();
            }
        }

        return maxes;
    }
}