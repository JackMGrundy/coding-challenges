"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# First attempt: Preorder traversal. 87th percetile in speed:
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None: return("")
        res = []
        out = self.helper(root, res)
        return(",".join(out))
    
    def helper(self, root, res):
        if root==None:
            return([])
        return([str(root.val)] + self.helper(root.left, res) + self.helper(root.right, res))
    
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="": return()
        data = data.split(",")
        data = [int(x) for x in data]
        curVal = data[0]
        root = TreeNode(curVal)
        curNode = root
        stack = [root]
        
        for i in range(1, len(data)):
            nextVal = data[i]
            nextNode = TreeNode(nextVal)
            
            #Moving left down the tree
            if nextVal < curVal:
                curNode.left = nextNode
            else:
                while stack and stack[-1].val < nextVal:
                    branchNode = stack.pop()
                branchNode.right = nextNode
                
            stack.append(nextNode)
            curNode = nextNode
            curVal = nextVal
        
        return(root)
                
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))