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
# 48ms. 82 percentile. 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return 
        elif nums == sorted(nums, key = lambda x: -x):
            nums.sort()
        else:
            # Find pivot index
            firstIndexAfterPivot = len(nums)-1
            while 0 < firstIndexAfterPivot and nums[firstIndexAfterPivot-1] >= nums[firstIndexAfterPivot]:
                firstIndexAfterPivot -= 1
            pivotIndex = firstIndexAfterPivot - 1
            pivot = nums[pivotIndex]
            
            # Find smallest number bigger than pivot that's also after pivot
            swapElement, swapIndex = min([ (num, i) for i,num in enumerate(nums[pivotIndex+1:], pivotIndex+1) if pivot < num ])
            
            # Swap pivot and next biggest element
            nums[pivotIndex], nums[swapIndex] = nums[swapIndex], nums[pivotIndex]
            nums[pivotIndex+1:] = sorted(nums[pivotIndex+1:])


"""
Notes:

General pattern...
1, 2, 3, 4
1, 2, 4, 3
1, 3, 2, 4
1, 3, 4, 2
1, 4, 2, 3
1, 4, 3, 2
2, 1, 3, 4
2, 1, 4, 3
2, 3, 1, 4
2, 3, 4, 1
2, 4, 1, 3
2, 4, 3, 1
3, 1, 2, 4


So at first we consider just the rightmost element...then the two rightmost elements...then the three most and so on...in each case we know that
we are extending to the next group when all the current numbers are in reverse order...

This repeats (all sorting is descending):

We don't just sort the last two...We have to sort the last two once once for each of the possible third to last elements...Similarly, we have to sort the last
three once for each of the elements as the fourth to last element (the pivot)

Immediately I think of it as 3 cases
The current group (the set of elements after the pivot) isn't sorted in descending order yet:
    The first (from right to left) time we see a decrease, we want to swap the smaller and bigger numbers
2, 1, 3, 4    ->   2, 1, 4, 3


The current group is sorted in descending order. We need to update the pivot. 
    To do this, we need the next largest number after the pivot. We can just swap the pivot with that number and then reverse the group

1, 4, 3, 2   ->    2, 1, 3, 4

Edge case...the whole array is sorted descending: 
    In that case just sort to reset

4, 3, 2, 1 -> 1, 2, 3, 4


We can actually think of the first two cases as one case and this makes everything very simple...
    We just find the first decreasing element, swap it with the next lagest element after it to the left, then we reverse all the elements after it. Ojala


"""