/*abstractYou have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
*/
// 1st attempt: 56th percentile. 68ms.
/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    if (logs === null || logs === undefined || logs.length===0) {
        return [];
    }
    
    let numberLogs = [];
    let letterLogs = [];
    
    logs.map(log => {
        if (!isNaN(log.split(" ")[1])) {
            numberLogs.push(log);
        } else {
            letterLogs.push(log);
        }
    });
    
    letterLogs.sort( (a,b) => a.split(" ").slice(1).join(" ").localeCompare( b.split(" ").slice(1).join(" ")) 
                              ||
                              a.split(" ").slice(0, 1).join(" ").localeCompare( b.split(" ").slice(0, 1).join(" ")));
    
    return letterLogs.concat(numberLogs);
};



// 2nd attempt: 74th percentile. 64ms.
/**
 * @param {string[]} logs
 * @return {string[]}
 */
var reorderLogFiles = function(logs) {
    if (logs === null || logs === undefined || logs.length===0) {
        return [];
    }
    
    let numberLogs = [];
    let letterLogs = [];
    
    logs.map(log => {
        if (!isNaN(log.split(" ")[1])) {
            numberLogs.push(log);
        } else {
            letterLogs.push(log);
        }
    });
    
    letterLogs.sort( (a,b) => a.substring(a.indexOf(" ")+1).localeCompare(b.substring(b.indexOf(" ")+1)) 
                                ||
                              a.substring(0, a.indexOf(" ")).localeCompare(b.substring(0, b.indexOf(" "))) );
    
    return letterLogs.concat(numberLogs);
};
