"""
Serialization is the process of converting a data structure or object into a sequence of 
bits so that it can be stored in a file or memory buffer, or transmitted across a network 
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted 
tree in which each node has no more than N children. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that an N-ary
 tree can be serialized to a string and this string can be deserialized to the original
  tree structure.

For example, you may serialize the following 3-ary tree

 



 

as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so please be creative
 and come up with different approaches yourself.

 

Note:

N is in the range of [1, 1000]
Do not use class member/global/static variables to store states. Your serialize and deserialize
algorithms should be stateless.
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# 564ms. 89 percentile.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        data = collections.deque([])
        
        def helper(root):
            if not root:
                return
            data.append(root.val)
            data.append(len(root.children))
            for child in root.children:
                helper(child)
        
        helper(root)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        else:
            val = data.popleft()
            children = data.popleft()
            root = Node(val, [ self.deserialize(data) for child in range(children) ])
            return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))




"""
Notes:

Very similar to serializing a binary tree. One hiccup is that we need to note how many children
each node has. We can simply store that value after each node's value. Then it's straight
preorder traversal. 
"""