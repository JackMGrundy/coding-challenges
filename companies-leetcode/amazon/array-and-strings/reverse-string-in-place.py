#!/usr/bin/python3
import sys

class Solution:
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        
        i=0
        while i!=len(s):
            j = i
            while j!=len(s) and s[j]!=" ":
                j+=1

            for k in range(i, j-(j-i)//2):
                s[k], s[j-(k-i)-1] = s[j-(k-i)-1], s[k]

            if j==len(s): return
            i = j+1



if __name__=='__main__':
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    sol = Solution()
    sol.reverseWords(s)