"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import heapq 

# Nlog(N) solution with plain sorting
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return(sorted(nums, reverse=True)[k-1])
        


# Solution with heap
class SolutionHeap(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return(-res)    



# 76ms. 80 percentile
# Pretty proud of that performance. Compares favorably even with built in one liners. 
# Quick Select Approach.
# How you're "supposed to do this"
# Best asymptotically. O(N) average with O(N^2) worst. 
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickSelect(nums, k)
    
    def quickSelect(self, nums, k):
        return self._quickSelect(nums, 0, len(nums)-1, k-1)

    def _quickSelect(self, nums, start, end, k):
        if start >= end:
            return nums[start]
        
        partitionIndex = self.partition(nums, start, end)
        if partitionIndex == k:
            return nums[partitionIndex]
        elif partitionIndex > k:
            return self._quickSelect(nums, start, partitionIndex-1, k)
        else:
            return self._quickSelect(nums, partitionIndex+1, end, k)

    def partition(self, nums, start, end):
        left = right = start
        
        # Select middle element to avoid sorted array hell
        partitionIndex = (start + end) // 2
        nums[end], nums[partitionIndex] = nums[partitionIndex], nums[end]
        
        while right < end:
            if nums[right] > nums[end]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        nums[left], nums[end] = nums[end], nums[left]
        return left
    
        
"""
Notes:

Core idea behind quick select is to do quicksort, but only recurse with whichever half of the partition has the kth
biggest element. 
"""