"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
Accepted
96,129
Submissions
228,367
"""
# 89th percentile. 56ms. 
# builtins.
from itertools import accumulate
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        res = 0
        matches = defaultdict(int) 
        matches[k] = 1
        
        forward = list(accumulate(nums))

        for x in forward:
            if x in matches:
                res += matches[x] 
            matches[x+k] += 1
        
        return res

# 89th percentile. 56ms. 
# no builtins
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums: 
            return 0
        res = 0
        matches = defaultdict(int) 
        matches[k] = 1
        sm = 0

        for n in nums:
            sm += n
            if sm in matches:
                res += matches[sm] 
            matches[sm + k] += 1
        
        return res


"""
Notes:

Say you have an arr and you have an array with cumulative sums for the array. Now let's say there are two 
cumulative sums that are the same. That means the sum of the values between them must be 0.

Extending this, say the different between the two is k, then the array between them must be k. 

So for every cumulative sum, we make that sum+k in a hashtable. Now we know that if we later see
such a sum, we've found an array with sum k.

Final bits

1) We don't just mark that we've seen this cumulative sum. Rather we count how many such
cumulative sums we've seen. 

2) We need to mark matches[k] equal to 1 to start. To see why we need this, imagine we didn't have it. We 
might march through an array with a sum equal to k, and we wouldn't recognize it as a match. 

"""