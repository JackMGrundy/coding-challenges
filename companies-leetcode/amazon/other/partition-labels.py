"""
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
# 36ms. 98th percentile.
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        starts = {}
        ends = {}
        for i, c in enumerate(S):
            if c not in starts:
                starts[c] = i
        for i in range (len(S)-1, -1, -1):
            c = S[i]
            if c not in ends:
                ends[c] = i
        
        characterRanges = [ (starts[c], ends[c]) for c in starts ]
        characterRanges.sort(key=lambda x: x[0])
        
        partitions = [-1]
        currentPartitionEnd = 0
        for characterRange in characterRanges:
            currentCharacterStart, currentCharacterEnd = characterRange
            if currentCharacterStart > currentPartitionEnd:
                partitions.append(currentPartitionEnd)
                currentPartitionEnd = currentCharacterEnd
            else:
                currentPartitionEnd = max(currentPartitionEnd, currentCharacterEnd)
        
        partitions.append(currentPartitionEnd)
        partitionSizes = [ partitions[i+1]-partitions[i] for i in range(len(partitions)-1) ]

        return partitionSizes