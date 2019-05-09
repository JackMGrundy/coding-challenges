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
// 13th percentile. 41ms. 
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
      HashMap<String, List> groups = new HashMap<String, List>();
      
      for (String s : strs) {
          char[] cs = s.toCharArray();
          Arrays.sort(cs);
          String key = new String(cs);
          if (!groups.containsKey(key)) {
              ArrayList<String> temp = new ArrayList<String>(); 
              temp.add(s);
              groups.put(key, temp);
          } else {
              List<String> temp = groups.get(key);
              temp.add(s);
              groups.put(key, temp);
          }
      }
      
      List<List<String>> res = new ArrayList<List<String>>();
      groups.forEach( (k,v) ->
                    res.add(v));
      
      return res;
  }
}



// 15th percentile 37ms.
// Just clarified generics
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
      HashMap<String, List<String>> groups = new HashMap<String, List<String>>();
      
      for (String s : strs) {
          char[] cs = s.toCharArray();
          Arrays.sort(cs);
          String key = new String(cs);
          if (!groups.containsKey(key)) {
              ArrayList<String> temp = new ArrayList<String>(); 
              temp.add(s);
              groups.put(key, temp);
          } else {
              List<String> temp = groups.get(key);
              temp.add(s);
              groups.put(key, temp);
          }
      }
      
      List<List<String>> res = new ArrayList<List<String>>();
      groups.forEach( (k,v) ->
                    res.add(v));
      
      return res;
  }
}

// 92nd percentile. 9ms
// So much faster with traditional for each loop
class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
      HashMap<String, List<String>> groups = new HashMap<String, List<String>>();
      
      for (String s : strs) {
          char[] cs = s.toCharArray();
          Arrays.sort(cs);
          String key = new String(cs);
          if (!groups.containsKey(key)) {
              ArrayList<String> temp = new ArrayList<String>(); 
              temp.add(s);
              groups.put(key, temp);
          } else {
              List<String> temp = groups.get(key);
              temp.add(s);
              groups.put(key, temp);
          }
      }
      
      List<List<String>> res = new ArrayList<List<String>>();
      for (String s : groups.keySet()) {
          res.add(groups.get(s));
      }
      
      return res;
  }
}