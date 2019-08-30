"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
# 1st attempt: 53rd percentile. Correct complexity O(N) 52 ms. 90th percentile is 44 ms.
# This solution uses two easy to understand N passes. 
# The faster approach uses a more confusing pincer approach...
class Solution:
    def trap(self, height: List[int]) -> int:
        guesses = [0]*len(height)
        peak = 0
        for i, v in enumerate(height):
            guesses[i] = max(0, peak-v)
            if v > peak:
                peak = v
        
        peak = 0
        for i in range(len(height)-1, -1, -1):
            v = height[i]
            guesses[i] = min(max(0, peak-v), guesses[i])
            if v > peak:
                peak = v
        
        return(sum(guesses))


# 2nd attempt: 99th percentile. pincer movement approach.
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height)<3: return 0
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        res = 0
        
        while l < r:
            lMax, rMax = max(lMax, height[l]), max(rMax, height[r])
            
            if lMax <= rMax:
                res += lMax - height[l]
                l += 1
            else:
                res += rMax - height[r]
                r -= 1
        
        return res
                
            
        
        