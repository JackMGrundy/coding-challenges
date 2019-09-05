"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""


# O(N^2)Log(N)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        validTriangles = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                curSum = nums[i]+nums[j]
                cutoff = bisect.bisect_left(nums, curSum)
                validTriangles += max(0, cutoff-j-1)
                
        return validTriangles
    
    
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        validTriangles = 0
        for i in range(len(nums)-1):
            k = i + 2
            for j in range(i+1, len(nums)):
                while k < len(nums) and nums[i]+nums[j] > nums[k]:
                    k += 1
                validTriangles += max(0, (k - j -1))
        
        return validTriangles