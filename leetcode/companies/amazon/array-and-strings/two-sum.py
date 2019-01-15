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