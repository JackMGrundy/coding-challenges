"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
# Solution with itertools
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        from collections import defaultdict
        import itertools
        
        if digits=="": return([])
        
        numToLet = defaultdict(list)
        numToLet["2"] = ["a", "b", "c"]
        numToLet["3"] = ["d", "e", "f"]
        numToLet["4"] = ["g", "h", "i"]
        numToLet["5"] = ["j", "k", "l"]
        numToLet["6"] = ["m", "n", "o"]
        numToLet["7"] = ["p", "q", "r", "s"]
        numToLet["8"] = ["t", "u", "v"]
        numToLet["9"] = ["w", "x", "y", "z"]

        digits = list(digits)
        inputs = [ numToLet[digit] for digit in digits ]
        res = list(itertools.product(*inputs))
        res = [ ''.join(item) for item in res]
        return(res)




# Solution without itertools
class Solution(object):
    
    def helper(self, res, mapping, digits, indx, cur):
        if indx==len(digits):
            res.append(cur)
            return
        else:
            for letter in mapping[digits[indx]]:
                self.helper(res, mapping, digits, indx+1, cur+letter )
        
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0: return([])
        mapping = {'2':'abc',
               '3':'def',
               '4':'ghi',
               '5':'jkl',
               '6':'mno',
               '7':'pqrs',
               '8':'tuv',
               '9':'wxyz'}
    
        res = []
        self.helper(res=res, mapping=mapping, digits=digits, indx=0, cur="")
        return(res)