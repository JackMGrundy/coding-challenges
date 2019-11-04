/*

Given a list of phrases, generate a list of Before and After puzzles.           

A phrase is a string that consists of lowercase English letters and spaces only.
No  space  appears in the start or the end of a phrase. There are no consecutive
spaces in a phrase.                                                             

Before  and  After  puzzles  are  phrases that are formed by merging two phrases
where  the  last  word  of the first phrase is the same as the first word of the
second phrase.                                                                  

Return  the  Before  and  After  puzzles that can be formed by every two phrases
phrases[i]  and  phrases[j]  where  i  != j. Note that the order of matching two
phrases matters, we want to consider both orders.                               

You should return a list of distinct strings sorted lexicographically.          

                                                                                

Example 1:                                                                      

Input: phrases = ["writing code","code rocks"]                                  

Output: ["writing code rocks"]                                                  

Example 2:                                                                      

Input: phrases = ["mission statement",                                          

                  "a quick bite to eat",                                        

                  "a chip off the old block",                                   

                  "chocolate bar",                                              

                  "mission impossible",                                         

                  "a man on a mission",                                         

                  "block party",                                                

                  "eat my words",                                               

                  "bar of soap"]                                                

Output: ["a chip off the old block party",                                      

         "a man on a mission impossible",                                       

         "a man on a mission statement",                                        

         "a quick bite to eat my words",                                        

         "chocolate bar of soap"]                                               

Example 3:                                                                      

Input: phrases = ["a","b","a"]                                                  

Output: ["a"]                                                                   

                                                                                

Constraints:                                                                    

1 <= phrases.length <= 100                                                      

1 <= phrases[i].length <= 100                                                   

*/

// 7ms. 74th percentile.
// Could fix autoboxing conversion in the phrases[i] + phrases[j]
// Could also be cleverer about the sorting part.
class Solution {
    public List<String> beforeAndAfterPuzzles(String[] phrases) {
        
        Map<String, List<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < phrases.length; i++) {
            String head = phrases[i].split(" ")[0];
            map.computeIfAbsent(head, s -> new ArrayList<>()).add(i);
        }
        
        Set<String> puzzles = new HashSet<>();
        
        for (int i = 0; i < phrases.length; i++) {
            String[] temp = phrases[i].split(" ");
            String tail = temp[temp.length - 1];
            if (map.containsKey(tail)) {
                for (Integer j : map.get(tail)) {
                    if (i != j) {
                        puzzles.add(phrases[i] + phrases[j].substring(tail.length()));
                    }
                }
            }
        }
        
        List<String> list = new ArrayList<>(puzzles);
        Collections.sort(list);
        
        return list;
    }
}


/*

Notes:

Iterate through the phrases. Make a mapping of words to list of phrases that start with the key word.
Instead of storing the phrases, store their indices.
Iterate through the phrases again. Get the last word in the current phrase. Get the list of phrases
that start with the last word. This could be a potential pair. To check, compare the index of the 
current phrase to the index of the possible match. If they aren't the same, we have a new match. 
Sort to deal with the lexicographically sorted requirement. 


Java specific:
computeIfAbsent is wonderful for populating maps whose values are data structures. We can
simply say to create a default data structure if it doens't exist yet, and then fluently
add values to it right away.


Problem specific:
Note that at first it might seem like we need to process each phrase twice, once using the
first word in the phrase and once using the last word in the phrase. But we don't. Just
picture the case of


"A B",  "B  C",  "C D"

Say we only try pairing by endings. Then we'll get both pairs as required. 

*/