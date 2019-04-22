"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""
# 81st percentile
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if not dict: return s
        if not s: return ""
        
        bolded = [ False for _ in s ]
        
        # Identify characters to be bolded
        for tag in dict:
            start = s.find(tag)
            while start != -1:
                for i in range(start, start + len(tag)):
                    bolded[i] = True
                # bolded[start:(start+len(tag))] = [True]*(start+len(tag))
                start = s.find(tag, start+1)
        
        # Construct output string
        bold = bolded[0]
        nxtString = "<b>" + s[0] if bold else s[0]
        res = ""
        
        for i in range(1, len(bolded)):                    
            # Finished a bold / non-bold section
            if bolded[i]!=bolded[i-1]:
                if bold:
                    res += nxtString + "</b>"
                    bold = False
                    nxtString = s[i]
                else:
                    res += nxtString
                    bold = True
                    nxtString = "<b>" + s[i]
                    
            # Continue constructing a section
            else:
                nxtString += s[i]
                        # End of string
            if i==len(s)-1:
                res = res + nxtString + "</b>" if bold else res + nxtString

        return res