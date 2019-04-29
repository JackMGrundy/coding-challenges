"""
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
"""
# Cheat and use built in methods...
# 89th percentile. 48ms.
"""
Uses a priority queue under the hood. So, O(N) to create and 
O(klog(N)) to retrieve for a total of
O(N + klog(N))
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = c.most_common(k)
        return [ x[0] for x in res ]