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
// 100th percentile
const topKFrequent = (nums, k) => {
    let map = new Map();
    
    // Count frequencies
    nums.forEach(num => {
        let cur = map.get(num);
        if (!cur) {
            map.set(num, {
                val : num,
                count : 1
            })
        } else {
            cur.count++;
        }
    })
    
    return Array.from(map.values())
                .sort( (a,b) => b.count - a.count )
                .slice(0, k)
                .map(o => o.val);
};