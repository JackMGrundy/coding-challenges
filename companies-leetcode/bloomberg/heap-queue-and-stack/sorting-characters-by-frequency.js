/*
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
*/
// 60ms. 99th percentile...very functional. 
/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let counts = s.split("").reduce( (a,b) => {
        a[b] = b in a ? a[b]+1 : 1;
        return a;
    }, {});
    let pairs = []
    for (let key in counts) {
        pairs.push([key, counts[key]]);
    }
    pairs.sort( (a,b) => {
        if (b[1] === a[1]) {
            return b[2]-a[2];
        } else {
            return b[1]-a[1];
        }
    });
    let res = pairs.reduce( (a,b) => {
        a.push(b[0].repeat(b[1]));
        return a;
    }, []);
    return res.join("");
};