"""
Given a binary tree, return the vertical order traversal of its nodes values.   

For  each node at position (X, Y), its left and right children respectively will
be at positions (X-1, Y-1) and (X+1, Y-1).                                      

Running  a  vertical  line  from  X  =  -infinity to X = +infinity, whenever the
vertical  line  touches  some  nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).                                  

If two nodes have the same position, then the value of the node that is reported
first is the value that is smaller.                                             

Return an list of non-empty reports in order of X coordinate.  Every report will
have a list of values of nodes.                                                 

                                                                                

Example 1:                                                                      

Input: [3,9,20,null,null,15,7]                                                  

Output: [[9],[3,15],[20],[7]]                                                   

Explanation:                                                                    

Without loss of generality, we can assume the root node is at position (0, 0):  

Then, the node with value 9 occurs at position (-1, -1);                        

The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);           

The node with value 20 occurs at position (1, -1);                              

The node with value 7 occurs at position (2, -2).                               

Example 2:                                                                      

Input: [1,2,3,4,5,6,7]                                                          

Output: [[4],[2],[1,5,6],[3],[7]]                                               

Explanation:                                                                    

The node with value 5 and the node with value 6 have the same position according
to the given scheme.                                                            

However,  in  the  report  "[1,5,6]", the node value of 5 comes first since 5 is
smaller than 6.                                                                 

                                                                                

Note:                                                                           

The tree will have between 1 and 1000 nodes.                                    

Each node's value will be between 0 and 1000.                                   

"""
# 40ms. 74 percentile. O(NlogN)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        stack, positions = [], collections.defaultdict(list)
        x, y = 0, 0
        while stack or root:
            if root != None:
                stack.append( (root, x, y) )
                x, y = x - 1, y + 1
                root = root.left
            else:
                node, x, y = stack.pop()
                root = node.right
                x, y = x + 1, y + 1
                positions[x].append( (x, y, node.val) )
        
        res = []
        for x in sorted(positions):
            res.append( [ node[2] for node in sorted(positions[x]) ] )
        return res


# 28ms. 99.87 percentile. O(Nlog(N))
# Avoids sort group sorts...less readable though
# Inorder traversal approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        stack, positions = [], []
        x, y = 0, 0
        while stack or root:
            if root != None:
                stack.append( (root, x, y) )
                x, y = x - 1, y + 1
                root = root.left
            else:
                node, x, y = stack.pop()
                root = node.right
                x, y = x + 1, y + 1
                positions.append( (x, y, node.val) )
        
        positions.sort()
        res = [ [] ]
        prevX = positions[0][0]
        for x, y, val in positions:
            if x != prevX:
                prevX = x
                res.append( [val] )
            else:
                res[-1].append(val)
                
        return res


"""
Notes:
This is actually a sorting problem. Lots of ways to do it. 

One way or another, we need to get a list of (x, y, node.val) for 
all the nodes. Then we organize them into groups based on the x
value. Finally we sort them based on y and then on node.val.

Any sort of traversal that allows tracking the x and y values
will work for getting the tuples. I used inorder traversal because
it makes the most intuitive sense to me. You could also use
another dfs variant or bfs though. 

"""