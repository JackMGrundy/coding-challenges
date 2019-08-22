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

class Solution {
    public String frequencySort(String s) {
        String[] sArr = s.split("");
        Map<String, Integer> counts = new HashMap<String, Integer>();
        for (String temp : sArr) {
            counts.put(temp, counts.getOrDefault(temp, 0)+1);
        }
        
        Comparator<String> charCountsComparator = new Comparator<String>() {
            
            public int compare(String a, String b) {
                if (counts.get(a) != counts.get(b)) {
                    return counts.get(b)-counts.get(a);
                } else {
                    return b.equals(a);
                }
            }
        };
        
        Arrays.sort(sArr, charCountsComparator);
            
        return String.join("", sArr);
    }
}