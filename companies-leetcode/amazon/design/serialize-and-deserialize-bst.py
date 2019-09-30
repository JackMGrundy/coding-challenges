"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# 60ms. 81 percentile.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        
        def helper(root):
            if not root:
                data.append("N,")
            else:
                data.append(str(root.val) + ",")
                helper(root.left)
                helper(root.right)

        helper(root)
        return ''.join(data)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(",")[0:-1])
        
        def helper():
            if not data:
                return None
            else:
                rootVal = data.popleft()
                if rootVal != 'N':
                    root = TreeNode(int(rootVal))
                    root.left = helper()
                    root.right = helper()
                    return root
        
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))