# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None: return(True)
        
        windowMaxes = {}
        windowMins = {} 
        windowMaxes[root] = float('inf')
        windowMins[root] = -float('inf')
        stack = [root]
        curNode = None
        
        while len(stack) > 0:
            curNode = stack.pop()
            
            # Left child
            if curNode.left:
                leftChild = curNode.left
            
                if (leftChild.val >= windowMaxes[curNode] or leftChild.val <= windowMins[curNode] or leftChild.val>=curNode.val):
                    return(False)

                windowMaxes[leftChild] = curNode.val
                windowMins[leftChild] = windowMins[curNode]
                stack.append(leftChild)
            
            # Right child
            if curNode.right:
                rightChild = curNode.right

                if (rightChild.val >= windowMaxes[curNode] or rightChild.val <= windowMins[curNode] or rightChild.val<=curNode.val):
                    return(False)

                windowMaxes[rightChild] = windowMaxes[curNode]
                windowMins[rightChild] = curNode.val 
                stack.append(rightChild)
        
        return(True)
        