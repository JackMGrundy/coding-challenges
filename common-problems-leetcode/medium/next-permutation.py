"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Accepted
231.5K
Submissions
762K
"""
# 99th percentile. 44 ms
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            pass
        elif nums == sorted(nums, reverse=True):
            nums.sort()
        else:
            pivotIndex = len(nums)-2            
            while pivotIndex >= 0:
                pivot = nums[pivotIndex]
                minItem = float("inf")
                minIndex = -1
                # get minitem to right of pivot
                for i in range(pivotIndex+1, len(nums)):
                    x = nums[i]
                    if x > pivot and x < minItem:
                        minItem = x
                        minIndex = i
                        
                
                # there is an item to the right of pivot that is greater than it
                if pivot < minItem < float("inf"):
                    nums[pivotIndex], nums[minIndex] = minItem, pivot
                    nums[pivotIndex+1:] = sorted(nums[pivotIndex+1:])
                    break
                else:
                    pivotIndex -= 1