/*
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
*/
// 5th percentile. 5136ms
// Amazingly bad solution
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  let groups = {};
  
  strs.forEach(s => {
      key = s.split('').sort().join('');
      if (Object.keys(groups).indexOf(key) === -1) {
          groups[key] = [s];
      } else{
          groups[key].push(s);
      }
  })
  
  let res = [];
  Object.keys(groups).forEach(group => {
      res.push(groups[group]);
  })
  return res;
};



// 94th percentile. 124 ms.
// Maps are once again the best thing ever
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  let groups = new Map()
  
  strs.forEach(s => {
      key = s.split('').sort().join('');
      if ( !groups.has(key) ) {
          groups.set(key, [s]);
      } else{
          groups.get(key).push(s)
      }
  })
  
  let res = [];
  groups.forEach(group => {
      res.push(group);
  })
  return res;
};