"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""
# 2nd attempt: 98th percentile in speed.
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if nums==[]: return(0)
        l = 0; sm = 0; res = float("inf")
        for r, num in enumerate(nums):
            sm += num
            while sm >= s:
                if r-l+1<res: res = r-l+1    
                if l==r: return(1)
                sm -= nums[l]
                l += 1        
 
        if res == float("inf"):
            return(0)
        else:
            return(res)
                
                
                
            