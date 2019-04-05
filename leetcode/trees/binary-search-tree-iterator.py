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
# Attempt 1:
"""
I started to store the last number returned...then I'd make a O(logn) call to find the next biggest
one. This doesn't work. Nonunique sequences will break it. Also too slow...need constant calls
"""


# Attempt 2: 99th percentile in speed
"""
Simple but cool takeaway from this. By making this class and saving the stack, you can turn 
traditional search algos into iterators. In this case, we're doing an in order traversal. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s = []
        while root: 
            self.s.append(root)
            root = root.left
            

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.s.pop()
        temp = cur.right
        while temp:
            self.s.append(temp)
            temp = temp.left
        return cur.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.s)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()