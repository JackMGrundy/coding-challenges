"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i in range(len(nums)):
            num = nums[i]
            compl = -(num-target)
            if compl in complements.keys():
                res = [i, complements[compl]]
                res.sort()
                return(res)
            complements[num] = i


if __name__=='__main__':
    sol = Solution()
    nums = [2,7,11,15]
    target = 9
    res = sol.twoSum(nums, target)
    print(res)


    
# Python3: 60ms. 100th percentile.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return -1
        validPartners = {}
        for i, num in enumerate(numbers, 1):
            if num in validPartners:
                return [validPartners[num], i]
            else:
                validPartners[target-num] = i
        
        return -1