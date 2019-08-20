/*
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
*/
// 60ms. 87th percentile
/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function(S) {
    let starts = {};
    let ends = {};
    for (let i = 0; i < S.length; i++) {
        let c = S[i];
        if (!(c in starts)) {
            starts[c] = i;
        }
    }
    for (let i = S.length-1; i >= 0; i--) {
        let c = S[i];
        if (!(c in ends)) {
            ends[c] = i;
        }
    }
    
    let characterRanges = [];
    for (let c in starts) {
        characterRanges.push( [starts[c], ends[c]] );
    }
    
    let partitions = [-1];
    let currentPartitionEnd = 0;
    for (let characterRange of characterRanges) {
        let currentCharacterStart = characterRange[0];
        let currentCharacterEnd = characterRange[1];
        if (currentCharacterStart > currentPartitionEnd) {
            partitions.push(currentPartitionEnd);
            currentPartitionEnd = currentCharacterEnd;
        } else {
            currentPartitionEnd = Math.max(currentPartitionEnd, currentCharacterEnd);
        }
    }
    partitions.push(currentPartitionEnd);
    
    let partitionSizes = [];
    for (let i = 0; i < partitions.length-1; i++) {
        partitionSizes.push
        (partitions[i+1]-partitions[i]);
    }
    
    return partitionSizes;
};