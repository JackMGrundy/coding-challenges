/*
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
*/

// 100ms. 95th percentile.
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    
    let helper = function(nums1, s1, e1, nums2, s2, e2, k) {
        
        if (e1 - s1 < 0) {
            return nums2[s2+k];
        }
        
        if (e2 - s2 < 0) {
            return nums1[s1+k];
        }
        
        if (k === 0) {
            return Math.min(nums1[s1], nums2[s2]);
        }
        
        let medianIndex1 = Math.floor((s1 + e1) / 2.0);
        let medianIndex2 = Math.floor((s2 + e2) / 2.0);
        let m1 = nums1[medianIndex1];
        let m2 = nums2[medianIndex2];
        
        if ( (medianIndex1 - s1) + (medianIndex2 - s2) < k) {
            
            if (m1 < m2) {
                return helper(nums1, medianIndex1+1, e1, nums2, s2, e2, k - (medianIndex1 - s1) - 1);
            } else {
                return helper(nums1, s1, e1, nums2, medianIndex2+1, e2, k - (medianIndex2 - s2) - 1);
            }
        } else {
            
            if (m1 > m2) {
                return helper(nums1, s1, medianIndex1-1, nums2, s2, e2, k);
            } else {
                return helper(nums1, s1, e1, nums2, s2, medianIndex2-1, k);
            }
        }
    }
    
    let totalNumElements = nums1.length + nums2.length;
    
    return (
        helper(nums1, 0, nums1.length-1, nums2, 0, nums2.length-1, Math.floor(totalNumElements / 2) )
        +
        helper(nums1, 0, nums1.length-1, nums2, 0, nums2.length-1, Math.floor( (totalNumElements-1) / 2) ) ) / 2.0;
};