/*
Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

 

Example 1:

Input: s = "owoztneoer"
Output: "012"
Example 2:

Input: s = "fviefuro"
Output: "45"
 

Constraints:

1 <= s.length <= 105
s[i] is one of the characters ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"].
s is guaranteed to be valid.
*/




//10th percentile
/**
 * @param {string} s
 * @return {string}
 */
 var originalDigits = function(s) {
    let sCharCounts = {}
    for (let i in s) {
        let char = s[i];
        char in sCharCounts ? sCharCounts[char]++ : sCharCounts[char] = 1;
    }
    
    let answerDigitCounts = Array(10).fill(0);

    
    // z only in zero
    answerDigitCounts[0] = sCharCounts['z'] || 0;
    // w only in two
    answerDigitCounts[2] = sCharCounts['w'] || 0;
    // u only in four
    answerDigitCounts[4] = sCharCounts['u'] || 0;
    // x only in six
    answerDigitCounts[6] = sCharCounts['x'] || 0;
    // g only in eight
    answerDigitCounts[8] = sCharCounts['g'] || 0;
    // h only in eight and three
    answerDigitCounts[3] = (sCharCounts['h'] || 0) - answerDigitCounts[8];
    // f only in four and five
    answerDigitCounts[5] = (sCharCounts['f'] || 0) - answerDigitCounts[4];
    // s only in six and seven
    answerDigitCounts[7] = (sCharCounts['s'] || 0) - answerDigitCounts[6];
    // i only in five, size, eight, and nine
    answerDigitCounts[9] = (sCharCounts['i'] || 0) - answerDigitCounts[5] - answerDigitCounts[6] - answerDigitCounts[8];
    // o only in zero, two, four, and one
    answerDigitCounts[1] = (sCharCounts['o'] || 0) - answerDigitCounts[0] - answerDigitCounts[2] - answerDigitCounts[4];
        
    let res = '';
    for (let i = 0; i < 10; i++) {
        res += (i + '').repeat(answerDigitCounts[i]);
    }
    
    return res;
    
};




// 100th percentile
var originalDigits = function(s) {
    var count = Array(10).fill(0);
    
    for(var i = 0; i < s.length; i++) {
        var c = s[i];
        if (c == 'z') count[0]++;
        if (c == 'w') count[2]++;
        if (c == 'x') count[6]++;
        if (c == 's') count[7]++; //7-6
        if (c == 'g') count[8]++;
        if (c == 'u') count[4]++; 
        if (c == 'f') count[5]++; //5-4
        if (c == 'h') count[3]++; //3-8
        if (c == 'i') count[9]++; //9-8-5-6
        if (c == 'o') count[1]++; //1-0-2-4
    }

    count[7] -= count[6];
    count[5] -= count[4];
    count[3] -= count[8];
    count[9] = count[9] - count[8] - count[5] - count[6];
    count[1] = count[1] - count[0] - count[2] - count[4];

    var sb = "";
    for(var i = 0; i <= 9; i++) {
        for(var j = 0; j < count[i]; j++) {
            sb+= i;
        }
    }
    return sb;
};