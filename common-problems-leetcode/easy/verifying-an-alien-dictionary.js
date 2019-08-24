/*
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
*/
// 56ms. 71st percentile.
/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    let ordering = order.split("").reduce( (a,b,i) => {
        a[b] = i;
        return a;
    }, {});
    
    for (let i = 0; i < words.length-1; i++) {
        let minLength = Math.min(words[i].length, words[i+1].length);
        let completelyMatch = true;
        for (let j = 0; j < minLength; j++) {
            let word1Char = ordering[words[i][j]]
            let word2Char = ordering[words[i+1][j]]
            if (word1Char < word2Char ) {
                completelyMatch = false;
                break;
            }
            else if (word1Char > word2Char) {
                return false;
            }
            else if (word1Char === word2Char) {
                continue;
            }
        }
        if (completelyMatch && words[i].length > words[i+1].length) {
            return false;
        }
    }
    
    return true;
};