"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
Accepted
323,183
Submissions
700,745
"""
# Quick/dirty implementation
# 61st percentile. 120 ms
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[str(sorted(s))].append(s)
        
        res = []
        for _,val in groups.items():
            res.append(val)
        return res

# 61st percentile. 120 ms
"""
Interesting that retrieving only the values is as fast as the keys and values...
maks intuitive sense
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[str(sorted(s))].append(s)
        
        res = []
        for val in groups.values():
            res.append(val)
        return res


# 61st percentile 120ms
# cleaner
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[str(sorted(s))].append(s)
        
        return list(groups.values())

# 90th percentile. 112ms
"""
little bit faster with join
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        
        return list(groups.values())