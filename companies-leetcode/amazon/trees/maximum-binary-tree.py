"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
"""
class TreeNode:
    def __init__(self, num):
        self.val = num
        self.right = None
        self.left = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in nums:
            nextNode = TreeNode(num)
            while stack and num>stack[-1].val:
                nextNode.left = stack.pop()
            if stack and stack[-1].val>num:
                stack[-1].right = nextNode
            stack.append(nextNode)
        
        return(stack[0])

if __name__=='__main__':
    myList = [3,2,1,6,0,5]
    sol = Solution()
    root = sol.constructMaximumBinaryTree(myList)