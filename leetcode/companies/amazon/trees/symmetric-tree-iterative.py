from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def symmetric(s):
    print(s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]: return(False)
    return(True)

class Solution:    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Edge cases
        if root in [ [], None]: return(True)
        if root.left==None and root.right==None: return(True)
        
        levels = {}
        levels[root] = 1
        q = deque([root])
        curNode = None
        curLevel = 1
        curLevelNodes = []
        endNodes = 0
        
        while q:
            curNode = q.popleft()
            
            if levels[curNode] == curLevel:
                if type(curNode)==int:
                    curLevelNodes.append('~')
                else:
                    curLevelNodes.append(curNode.val)
            else:
                #Check if the last level was symmetric
                check = symmetric(curLevelNodes)
                if not check: return(False)
                
                #Reset
                curLevel += 1
                if type(curNode)==int:
                    curLevelNodes = ['~']
                else:
                    curLevelNodes = [curNode.val]
                    
            #Add children
            if type(curNode)!=int:
                for c in [curNode.left, curNode.right]:
                    if c:
                        levels[c] = curLevel+1
                        q.append(c)
                    else:
                        endNodeHash = hash(endNodes)
                        levels[endNodeHash] = curLevel+1
                        endNodes += 1
                        q.append(endNodeHash)
        
        #Check last level
        check = symmetric(''.join(curLevelNodes))
        if not check: return(False)   
        
        return(True)
            
            
            
        