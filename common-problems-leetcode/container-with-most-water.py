"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Accepted
353.5K
Submissions
805.1K
"""
# Timeout: Tried super quick O(N^2) brute force as a benchmark
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h = len(height); res = 0
        
        for j in range(h):
            for i in range(h):
                res = max(res, min(height[j], height[i])*abs(j-i))
        
        return res


# 59th percentile. 68ms
class Solution:
    def maxArea(self, height: List[int]) -> int:
        tail = res = 0
        head = len(height)-1
        
        while tail != head:
            res = max(res, min(height[tail], height[head])*abs(head-tail))
            if height[tail] < height[head]:
                tail += 1
            else:
                head -= 1
        
        return res
            
