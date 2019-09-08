"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
# 132ms. 91st percentile. 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        
        for num in nums:
            if count1 == 0 and num != candidate2:
                candidate1, count1 = num, 1
            elif count2 == 0 and num != candidate1:
                candidate2, count2 = num, 1
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [candidate for candidate in (candidate1, candidate2)
                    if nums.count(candidate) > len(nums) // 3]


"""
Notes:
See notes on Boyer Moore

This is a modified version of BM. Most it is straightforward. We're just maintaining counts for two different candidates. 
Cases:

-) we need a new candidate because count is zero
simple, just set the new candidate...make sure its not already set as the other candidate

-) next num doesn't match either candidate
pretty intuititve. Decrease both counts by 1

-) next num matches one of the two candidates
The only tricky one in my opinion. It's clear we increase count for the one that matches. But what about the other one?
Do we decrease that one? If we do, the algorithm doesn't work. 
So why don't we?

Example:
[1, 3, 5, 1, 3, 6, 7, 1, 3]
Matches are 1 and 3

Let's say all we care about are:
correct votes: votes that increase 1 and 3 or decrease another value
incorrect votes: votes that decrease 1 and 3 or increase another value

If there's 1 true candidate, we'll have at least n//3 corrects
If there's 2 true candidates we'll have at least 2n//3 corrects

The matches are simple. They are either using up a correct or an incorrect vote. 

The misses on both candidate are trickier. We decrease counts by 2 total. This could be using up 2 corrects, 2 incorrects, or 1 of each. 

It's like an amortized analysis problem....

Need to run through this again to solidify intuition...

"""