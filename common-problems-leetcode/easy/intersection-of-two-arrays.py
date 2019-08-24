"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""
# 44ms. 99th percentile.
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        matches = set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            if num in s:
                matches.add(num)
        res = []
        for num in matches:
            res.append(num)
        
        return res