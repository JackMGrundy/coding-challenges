"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Accepted
89.8K
Submissions
227.7K
"""

# 88ms. 99.999 percentile
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        res, sortedNums = [], []
        for num in nums[::-1]:
            i = bisect.bisect_left(sortedNums, num)
            res.append(i)
            # bisect.insort_left(sortedNums, num)  # ~85-95th percentile
            sortedNums[i:i] = num,  # 100th percentile
            # sortedNums = sortedNums[:i] + [num] + sortedNums[i:]  # 5th percentile...new list created
            
        return res[::-1]


# Merge sort idea:

# Start with plain merge sort
class Solution:
    def countSmaller(self, nums):
        def mergeSort(nums):
            half = len(nums) // 2
            if half:
                left, right = mergeSort(nums[:half]), mergeSort(nums[half:])
                # for i in range(len(nums))[::-1]: # Equivalently
                for i in range( len(nums) - 1, -1, -1):
                    if not right or left and left[-1] > right[-1]:
                        nums[i] = left.pop()
                    else:
                        nums[i] = right.pop()
            return nums

        nums = mergeSort(nums)
        return nums


# Then adjust for this problem:
# 168ms. 61 percentile.
class Solution:
    def countSmaller(self, nums):
        def mergeSort(nums):
            half = len(nums) // 2
            if half:
                left, right = mergeSort(nums[:half]), mergeSort(nums[half:])
                for i in range(len(nums))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        nums[i] = left.pop()
                    else:
                        nums[i] = right.pop()
            return nums
        
        smaller = [0]*len(nums)
        mergeSort(list(enumerate(nums)))
        return smaller



"""
Notes:

	First idea:

	Start a descending sorted list

	Go through the nums in reverse order
		Use binary search to figue out at what index the element should go O(log(N))

		NumElements in list - that index = the number that are less than the current element after it

		Insert the number into its place in the list O(C)
		...this could be problematic depending on the language...how to do this exactly...linked list yields constant
		insertion...but then how to do the binary search

        In python we can just use bisect
	O(Nlog(N))




    Cool idea from Pochman

        Given a stable sort......the only time a value gets "flipped" to the other side of a 
        pivot is when it's less than the pivot. Therefore, we can do a stable sort and record 
        how often a value is flipped around each pivot. 
        O(Nlog(N))

        Quick sort isn't stable, neither is heap sort, but merge sort is.  

        Steps:
        Keep a memo with a spot for each element of the array...each element records how many 
        smaller elements there are to the right of that element

        Keep recursing while splitting the array in half at each level...bottom is when we get 
        an array with no elements...

        Then at each level...iterate through the total length of the array (including both left 
        and right). 

        Now for the key bit within this loop. Typical merge sort, we check if the top of left 
        is greater than the top of right. If it is, we would take the top of right instead of 
        left (for an ascending sort)...this signifies a swap and therefore an element to the 
        right of left that is less than it. So this is the case where we increment the memo.
        Note, this case is triggered if right is empty...in this case the remaining elements of 
        left are all bigger than the already popped elements who were jumped...meaning the last 
        right element popped effectively jumped all the remaining left elements...so we increment
        them

        In the case left is empty or the right element is greater than or equal to the top left 
        element, we just pop the right element as it won't hop over the left one. 

        That's the meat and potatoes. For some finer points:
        When we actually increment the memo, we need to know the index of the left element that
        was jumped. We can do this by iterating over a list of (val, index) pairs instead of 
        just the list of values. For java just make a little class, create pairs for all the 
        vals, and then perform merge sort on that list. For javascript, make lists for the 
        pairs. For Python you can just use enumerate. 
"""