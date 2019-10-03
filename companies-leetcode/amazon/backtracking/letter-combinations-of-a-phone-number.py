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
# 8ms. 99th percentile. 
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
        return res




# Solution without itertools
# 12ms. 94th percentile.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        possibleCombinations = []
        
        digitToLetters = { "0": [], "1": [], "2": ["a", "b", "c"], "3": ["d", "e", "f"], 
                          "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], 
                          "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"], }
        
        def backtrack(i, path):
            if i == len(digits):
                possibleCombinations.append( ''.join(path) )
                return
            
            for letter in digitToLetters[digits[i]]:
                backtrack(i + 1, path + [letter])
        
        backtrack(0, [])
        
        return possibleCombinations


"""
Notes:

Standard backtracking

"""
        