"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Accepted
131,021
Submissions
353,568
"""
# Attemp 1: 30th percentile in speed
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [ sum(nums[0:(x+1)]) for x in range(len(nums)) ]

    def sumRange(self, i: int, j: int) -> int:
        if i==0: return self.nums[j]
        return self.nums[j] - self.nums[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# Attempt 2: 76th percentile in speed.
# Tiny bit messier, but much faster (avoid repeated sub sums)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1] 

    def sumRange(self, i: int, j: int) -> int:
        if i==0: return self.nums[j]
        return self.nums[j] - self.nums[i-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)



# 99th percentile solutions are like 50MS vs 54MS like this one^. And as far as I can tell, it's just a timer issue.  