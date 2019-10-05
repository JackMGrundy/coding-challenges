"""
Given an array w of positive integers, where w[i] describes the weight of 
index i, write a function pickIndex which randomly picks an index in 
proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution's constructor has one argument, the array w. pickIndex has no 
arguments. Arguments are always wrapped with a list, even if there 
ren't any.

Accepted
24,452
Submissions
57,249
"""
# 272ms. 91 percentile.
# Custom binary search
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        for i in range(len(w)):
            w[i] = w[i]/total
            if 0 < i:
                w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        randVal = random.random()
        index = self.binarySearch(self.w, randVal)
        return index
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = left + (right - left)//2
            
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



# 99th percentile. 192 ms.
# built ins.
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        for i in range(len(w)):
            w[i] = w[i]/total
            if 0 < i:
                w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        randVal = random.random()
        index = bisect.bisect_left(self.w, randVal)
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


"""
Notes:

Boils down to making a cumulative distribution, generating a random
value and then select the corresponding group.

"""