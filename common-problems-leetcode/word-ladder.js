/*
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
Accepted
249.3K
Submissions
1.1M
*/
// 95th percentile. 124 ms.
/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    
    if (wordList.indexOf(endWord) === -1 || !beginWord || !endWord | wordList.length===0) return 0;
    
    // Construct dict of intermediate states;
    let interWords = new Map();
    const L = beginWord.length;
    wordList.forEach(word => {
        for (let i = 0; i < L; i++) {
            let key = word.slice(0, i) + "*" + word.slice(i+1, L);
            if (!interWords.has(key)) {
                interWords.set(key, []);
            }
            let temp = interWords.get(key);
            temp.push(word);
        }
    });
    
    // BFS
    let q = [];
    q.push( { cur: beginWord, d: 1} );
    let visited = new Set();
    visited.add(beginWord);
    while (q.length > 0) {
        const {cur, d} = q.shift();
        
        for (let i = 0; i < L; i++) {
            let interWord = cur.slice(0, i) + "*" + cur.slice(i+1, L);
            let nxtWords = interWords.get(interWord);
            if (!nxtWords) continue;
            
            for (let w = 0; w < nxtWords.length; w++) {
                let word = nxtWords[w];
                if (!visited.has(word)) {
                    if (word === endWord) return d+1;
                    visited.add(word);
                    q.push( { cur: word, d: d+1 } );
                }
            }
        }
    }
    return 0;
};