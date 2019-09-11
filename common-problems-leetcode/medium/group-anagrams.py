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

# 148ms 12 percentile.
# Technically the best asymptotically, but slower due to testing string sizes
# and constant factors. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        
        for s in strs:
            key = [ 0 for _ in range(26) ]
            for c in s:
                key[ord(c) - ord('a')] += 1
            groups[tuple(key)].append(s)
        
        return groups.values()


"""
Notes:

It's Klog(K) to sort each string. the last approach is technically faster because it's just K...no sorting.

"""