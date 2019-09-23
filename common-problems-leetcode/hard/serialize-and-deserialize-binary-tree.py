"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""
# Attempt 1: 82 percentile. 60ms. 
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
        if not root:
            return ""
        res = []
        def helper(root):
            if not root:
                res.append("N,")
                return
            res.append(str(root.val)+",")
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ''.join(res)
            
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        def helper():
            if not data:
                return
            val = data.popleft()
            if val == "N":
                return
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        
        data = collections.deque(data.split(","))
        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


"""
Notes:
	Per usual with tree problems, big piece is figuring out what traversal method to use. In this case preorder is 
    the way to go. 

	The serialization is straightforwards...especially with recursion...it's just "add root to string...make 
    recursive call to left, make recursive call to right."

	For the deserialization:
	This can be a bit harder to recall, but two simple things save the day:
	1) in the serialized list, a node's left will always be right after it. 
	2) recursion
	

	Given these, the actual recursive method is super straightforwards. You just pop the far left node 
    (enter queue/deque), then set its left equal to a recursive call.
	Finally set its right equal to another recursive call. It's actually a really cool mirror of preoder traversal. 
	"Pop the root node...attach its left...recursive calls will continue to be spun up to attach more lefts 
    until they're aren't more lefts. Then the bottom recursive call will try to attach the right node...and so on as we 
    unwind the call stack."


	Example:
	1,2,3,None,None,4,None,None,5,None,None


    Note you do need the commas because of negative numbers...relying on a method like 
    collections.deque(data) to split the data will break with negative numbers.
"""