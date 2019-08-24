"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

# 108ms. 71st percentile.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findKth(nums1, s1, e1, num2, s2, e2, k):
            if e1 - s1 < 0:
                return nums2[s2+k]
            
            if e2 - s2 < 0:
                return nums1[s1+k]
            
            if k == 0:
                return min(nums1[s1], nums2[s2])
            
            medianIndex1, medianIndex2 = (s1 + e1) // 2, (s2 + e2) // 2
            m1, m2 = nums1[medianIndex1], nums2[medianIndex2]

            if (medianIndex1 - s1) + (medianIndex2 - s2) < k:
                if m1 < m2:
                    return findKth(nums1, medianIndex1+1, e1, nums2, s2, e2, k - (medianIndex1 - s1) - 1)
                else:
                    return findKth(nums1, s1, e1, nums2, medianIndex2+1, e2, k - (medianIndex2 - s2) - 1)
            else:
                if m1 > m2:
                    return findKth(nums1, s1, medianIndex1-1, nums2, s2, e2, k)
                else:
                    return findKth(nums1, s1, e1, nums2, s2, medianIndex2-1, k)
        
        totalNumElements = len(nums1) + len(nums2)
        return ( findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, totalNumElements // 2)
                    +
                findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (totalNumElements-1) // 2) ) / 2.0
        
        
                
"""
I found the details of this very hard to get right...like hours of time...To my future self, here is a version with excessive comments. 
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findKth(nums1, s1, e1, num2, s2, e2, k):
            
            # have we eliminated all of the elements in either array? If so, we can pick the
            # kth element from the other
            if e1 - s1 < 0:
                return nums2[s2+k]
            
            if e2 - s2 < 0:
                return nums1[s1+k]
            
            # we want the next element. So it must be the smallest of num1 and num2's next elements. 
            if k == 0:
                return min(nums1[s1], nums2[s2])
            
            # Not true median but that's ok. We just need to be able to determine if the 
            # the final median is on the left side or right side. This lets us lop off
            # half (within +-1 element) of the elements in each call
            medianIndex1, medianIndex2 = (s1 + e1) // 2, (s2 + e2) // 2
            m1, m2 = nums1[medianIndex1], nums2[medianIndex2]
            
            # Is there k stuff on the left side or the right side...
            # If there's k stuff on the right side of our partition, then
            # k must be on that side...converse applies too
            if (medianIndex1 - s1) + (medianIndex2 - s2) < k:
                # There's k stuff on the right hand side.
                # We can ditch the left hand side of whichever array's "median" is smaller... 
                # we know those elements couldn't possibly be the kth element
                if m1 < m2:
                    # Adjust k to reflect that we lopped off elements...so now we have reduced the problem to finding
                    # the k - stuff we lopped off in one unchanged array and one somewhat smaller array
                    return findKth(nums1, medianIndex1+1, e1, nums2, s2, e2, k - (medianIndex1 - s1) - 1)
                else:
                    return findKth(nums1, s1, e1, nums2, medianIndex2+1, e2, k - (medianIndex2 - s2) - 1)
            else:
                # There's k stuff on the left hand side
                # We can ditch the right hand side of whichever array's median value is bigger
                if m1 > m2:
                    # We don't need to adjust k. We cut off stuff from the end of the arrays. We still want
                    # the kth element in the unchanged array and the shortened array
                    return findKth(nums1, s1, medianIndex1-1, nums2, s2, e2, k)
                else:
                    return findKth(nums1, s1, e1, nums2, s2, medianIndex2-1, k)
        
        totalNumElements = len(nums1) + len(nums2)
        return ( findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, totalNumElements // 2)
                    +
                findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (totalNumElements-1) // 2) ) / 2.0
        
        
                

# With some print statements:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findKth(nums1, s1, e1, num2, s2, e2, k):
            print(nums1[s1:e1+1], num2[s2:e2+1], k)
            # have we eliminated all of the elements in either array? If so, we can pick the
            # kth element from the other
            if e1 - s1 < 0:
                return nums2[s2+k]
            
            if e2 - s2 < 0:
                return nums1[s1+k]
            
            # we want the next element. So it must be the smallest of num1 and num2's next elements. 
            # It may seem unintuitive that 0 marks "next element", but that's because all the indexing
            # is array indexing with 0 meaning the first element
            if k == 0:
                return min(nums1[s1], nums2[s2])
            
            # Not true median but that's ok. We just need to be able to determine if the 
            # the final median is on the left side or right side. This lets us lop off
            # half (within +-1 element) of the elements in each call
            medianIndex1, medianIndex2 = (s1 + e1) // 2, (s2 + e2) // 2
            m1, m2 = nums1[medianIndex1], nums2[medianIndex2]
            print("1: ", s1, medianIndex1, e1)
            print("2: ", s2, medianIndex2, e2)
            print("ms: ", m1, m2)
            print("k: ", k)
            print("(medianIndex1 - s1) + (medianIndex2 - s2): ", (medianIndex1 - s1) + (medianIndex2 - s2), "\n")
            
            # Is there k stuff on the left side or the right side...
            # If there's k stuff on the right side of our partition, then
            # k must be on that side...converse applies too
            if (medianIndex1 - s1) + (medianIndex2 - s2) < k:
                # There's k stuff on the right hand side.
                # We can ditch the left hand side of whichever array's "median" is smaller... 
                # we know those elements couldn't possibly be the kth element
                if m1 < m2:
                    # Adjust k to reflect that we lopped off elements...so now we have reduced the problem to finding
                    # the k - stuff we lopped off in one unchanged array and one somewhat smaller array
                    return findKth(nums1, medianIndex1+1, e1, nums2, s2, e2, k - (medianIndex1 - s1) - 1)
                else:
                    return findKth(nums1, s1, e1, nums2, medianIndex2+1, e2, k - (medianIndex2 - s2) - 1)
            else:
                # There's k stuff on the left hand side
                # We can ditch the right hand side of whichever array's median value is bigger
                if m1 > m2:
                    # We don't need to adjust k. We cut off stuff from the end of the arrays. We still want
                    # the kth element in the unchanged array and the shortened array
                    return findKth(nums1, s1, medianIndex1-1, nums2, s2, e2, k)
                else:
                    return findKth(nums1, s1, e1, nums2, s2, medianIndex2-1, k)
        
        totalNumElements = len(nums1) + len(nums2)
        return ( findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, totalNumElements // 2)
                    +
                findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (totalNumElements-1) // 2) ) / 2.0


"""
Examples output for:
[1,7,8,9,10]
[2,4, 5, 11]

9 4
[1, 7, 8, 9, 10] [2, 4, 5, 11] 4
1:  0 2 4
2:  0 1 3
ms:  8 4
k:  4
(medianIndex1 - s1) + (medianIndex2 - s2):  3 

[1, 7, 8, 9, 10] [5, 11] 2
1:  0 2 4
2:  2 2 3
ms:  8 5
k:  2
(medianIndex1 - s1) + (medianIndex2 - s2):  2 

[1, 7] [5, 11] 2
1:  0 0 1
2:  2 2 3
ms:  1 5
k:  2
(medianIndex1 - s1) + (medianIndex2 - s2):  0 

[7] [5, 11] 1
1:  1 1 1
2:  2 2 3
ms:  7 5
k:  1
(medianIndex1 - s1) + (medianIndex2 - s2):  0 

[7] [11] 0
"""
