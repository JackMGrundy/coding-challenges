class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s.reverse()
        return(''.join(s))
        