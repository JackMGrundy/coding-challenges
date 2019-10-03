"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack or self.root:
            if self.root:
                self.stack.append(self.root)
                self.root = self.root.left
            else:
                node = self.stack.pop()
                self.root = node.right
                break
        
        return node.val if node else None
            

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.root


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


"""
Notes:

Iterative in order traversal. After getting the next smallest value, we save the stack and the
current root and then stop the traversal. 

"""