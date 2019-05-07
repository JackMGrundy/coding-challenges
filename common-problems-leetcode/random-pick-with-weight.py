"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

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

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

Accepted
24,452
Submissions
57,249
"""
# 53rd percentile. 300ms.
from random import randint
class Solution:
    
    def __init__(self, w: List[int]):
        self.indexCutoffs = [0]*len(w)
        self.indexCutoffs[0] = w[0]
        for i in range(1, len(w)):
            self.indexCutoffs[i] += self.indexCutoffs[i-1]  + w[i]
        self.totalWeight = self.indexCutoffs[-1]

    def pickIndex(self) -> int:
        target = randint(1, self.totalWeight)
        l, r = 0, len(self.indexCutoffs)-1
        while l < r:
            mid = (l+r)//2
            if self.indexCutoffs[mid] >= target:
                r = mid
            else:
                l = mid+1
        return l
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



# 97th percentile. 184 ms.
from random import random
from bisect import bisect_left
class Solution:
    
    def __init__(self, w: List[int]):
        totalWeight = sum(w)
        self.indexCutoffs = []
        cumulativeSum = 0
        for weight in w:
            cumulativeSum += float(weight)/totalWeight
            self.indexCutoffs.append(cumulativeSum)
            
    def pickIndex(self) -> int:
        target = random()
        test = bisect_left(self.indexCutoffs, target)
        return test

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()