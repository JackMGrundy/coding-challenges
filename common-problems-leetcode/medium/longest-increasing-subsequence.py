"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

# Timeout
# N^2 memoization approach
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        memo = [ [ -1 for x in range(len(nums))] for y in range(len(nums)) ]
        
        def dp(nums, memo, prevIndex, curIndex):
            if curIndex == len(nums):
                return 0
            
            if (memo[prevIndex][curIndex] >= 0):
                return memo[prevIndex][curIndex]
            
            taken = 0
            if prevIndex == -1 or nums[prevIndex] < nums[curIndex]:
                taken = 1 + dp(nums, memo, curIndex, curIndex+1)
            
            notTaken = dp(nums, memo, prevIndex, curIndex+1)
            
            memo[prevIndex][curIndex] = max(taken, notTaken)
        
            return memo[prevIndex][curIndex]
    
    
        return dp(nums, memo, -1, 0)


# N^2. N space memoization approach. 
# 1120 33ms.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [ 1 for x in nums ]
        bestOverall = 0
        
        for i in range(len(nums)):
            curElement = nums[i]
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        return max(dp)


# Nlog(N) dp-binary search approach
# 44ms. 97th percentile. 
# Note the extra binary search found case...
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [ -float("inf") ]
        
        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                index = self.binarySearch(dp, 0, len(dp)-1, num)
                dp[index] = num
        
        return len(dp)-1
        

    def binarySearch(self, nums, l, r, target):
        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m
                        
            elif nums[m] < target < nums[m+1]:
                return m+1
            
            elif nums[m] < target:
                l = m+1
                
            elif target < nums[m]:
                r = m-1
    

# Using builtins for binary search...
# 36ms. 99.9th percentile.
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [ -float("inf") ]
        
        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                index = bisect_left(dp, num)
                dp[index] = num
        
        return len(dp)-1


"""
Notes:

First option is to brute force it. Trying all the different subsequences. You can see this is 2^N, because for each
element, we can have take it or leave it, so 2*2*2...N times => 2^N. 
In more detail, at each element we make two recusive calls, one that includes that current element and one that doesn't. At each
level of recursion, we just take the best one. 

Second option is to memoize. We make a N*N memo where 1 dimension is the last element taken and the other is the current
element being considered. The size of memo makes it apparent this is N^2. Another way to see that, we have N choose 2
different combos...so  N! / 2!(N-2)! = N(N-1)/2 => N^2

Third option is to memoize more intelligently. 
We have a 1-d N length memo. Each element says "this is the longest subsequence that can be achieved up to this
point using this element. 
Building this up is straightforwards. To generate dp[i], we compare the current element to every preceding dp element.
We take whatever is the longest one that we can legally append to. So for every element we do at most N work
meaning this is still O(N^2)...but space is only O(N). 


Fourth option: O(NLog(N)) option. Dp with binary search
Key idea, we can maintain a series of sequences of differing lengths. I.e. we keep the "best" 2 element sequence, the "best"
3 element sequence and so on. The "best" such sequence is the one that is an increasing subsequence with the smallest
end element. So as wek go through, the elements, we maintain these lists. 

For each of the lists, if the current element is less than its end, we can ditch that list. 

So far, this approach is still N^2...for each element we can examine up to N lists....

The insight is that we can drop is to Olog(N) by using binary search to figure out where to insert the next
element. 

For example, let's say this was our series of "best" arrays:


0
0, 2
0, 2, 5
0, 2, 5, 8

if we see "4" then that can replace 5 in the best length 3 array. If we see 9, we add a new length 5 array. 
And so on. 

Each new number can only impact 1 of the arrays, so binary search works fine. 

The final icing on the cake - We don't actually need to store a bunch of different arrays. We can just store a single
N dimensional array that records the ends of the best arrays. 

"""