"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""
class TreeNode:
    def __init__(self, num):
        self.val = num
        self.right = None
        self.left = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        sList = [',']
        tList = [',']
        for nextTree in [(s, sList), (t, tList)]:
            root, stringRep = nextTree
            stack = [root]
            while stack:
                curNode = stack.pop()
                stringRep.append(str(curNode.val)+",")
                if curNode.val != None:
                    for c in [curNode.right, curNode.left]:
                        if c == None: 
                            stack.append(TreeNode(None))
                        else:
                            stack.append(c)

        tList = ''.join(tList)
        sList = ''.join(sList)
        return(tList in sList)