/*
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
*/

// 285ms. 14th percentile.
import java.util.*;
class TrieNode {
    TrieNode[] children;
    int times;
    
    public TrieNode() {
        this.children = new TrieNode[27];
        this.times = 0;
    }
    
    public String toString() {
        char[] alphabet = new char[27];
        StringBuilder s = new StringBuilder();
        for (int i = 0; i <  26; i++) {
            if (this.children[i] != null) {
                String nxt = String.valueOf( (char) (i+97) );
                s.append(nxt + ", ");
            } else {
                s.append("_, ");
            }
        }  
        s.append(". times: " + this.times); 
        return s.toString();
    }
    
}

class AutocompleteSystem {
    TrieNode trie;
    String currentSearch;
    TrieNode currentSearchRoot;
    List<String> currentRecommendations;
    Map<String, Integer> sentenceCounts;
        
    public AutocompleteSystem(String[] sentences, int[] times) {
        this.trie = createTrie(sentences, times);
        this.currentSearch = "";
        this.currentSearchRoot = this.trie;
        this.currentRecommendations = new ArrayList<String>();
        this.sentenceCounts = new HashMap<String, Integer>();
    }
    
    public TrieNode createTrie(String[] sentences, int[] times) {
        TrieNode trie = new TrieNode();
        TrieNode root;
        int sentenceId = 0;
        for (String sentence : sentences) {
            root = trie;
            for (char c : sentence.toCharArray()) {
                int charIndex;
                if (c == ' ') {
                    charIndex = 26;
                } else {
                    charIndex = c-'a';    
                }
                
                if (root.children[charIndex] == null) {
                    root.children[charIndex] = new TrieNode();
                }
                root = root.children[charIndex];
            }
            root.times = times[sentenceId++];
        }    
        return trie;
    }
    
    public void insertSentence(String sentence) {
        TrieNode root = this.trie;
        for (char c : sentence.toCharArray()) {
            int charIndex;
            if (c == ' ') {
               charIndex = 26; 
            } else {
                charIndex = c-'a';
            }
            
            if (root.children[charIndex] == null) {
                root.children[charIndex] = new TrieNode();
            }
            root = root.children[charIndex];
        }
        root.times++;
    }
    
    
    public List<String> input(char c) {
        int cIndex = (c == ' ') ? 26 : c-'a';
        
        if (c == '#') {
            insertSentence(this.currentSearch);
            this.currentSearch = "";
            this.currentRecommendations = new ArrayList<String>();
            this.currentSearchRoot = this.trie;
            return new ArrayList<String>();
        } else if (this.currentSearchRoot.children[cIndex]==null) {
            this.currentSearch += String.valueOf(c);
            this.currentRecommendations = new ArrayList<String>();
            this.currentSearchRoot = new TrieNode();
            return this.currentRecommendations;
        } else {
            this.currentSearch += String.valueOf(c);
            this.currentSearchRoot = this.currentSearchRoot.children[cIndex];
            this.updateRecommendations();
            return this.currentRecommendations;
        }
    }
    
    public void updateRecommendations() {
        this.sentenceCounts = new HashMap<String, Integer>();
        this.currentRecommendations = new ArrayList<String>();
        updateSentenceCounts(this.currentSearchRoot, "");
        
        Comparator<String> sentenceComparator = new Comparator<String>() {
            
            public int compare(String a, String b) {
                if (sentenceCounts.getOrDefault(a, 0) != sentenceCounts.getOrDefault(b, 0)) {
                    return sentenceCounts.getOrDefault(b, 0) - sentenceCounts.getOrDefault(a, 0);
                } else {
                    return a.compareTo(b);
                }
            }
        };
        
        PriorityQueue<String> pq = new PriorityQueue<String>(sentenceComparator);
        for (Map.Entry<String, Integer> entry : this.sentenceCounts.entrySet()) {
            pq.offer(entry.getKey());
        }
        while (pq.size() > 0) {
            String nxt = pq.poll();
            this.currentRecommendations.add(nxt);
            if (this.currentRecommendations.size() >= 3) {
                return;
            }
        }
    }
    
    
    public void updateSentenceCounts(TrieNode root, String sentence) {        
            
        if (root.times > 0) {
            this.sentenceCounts.put(this.currentSearch + sentence, root.times);
        }
        
        for (int i = 0; i < 27; i++) {
            if (root.children[i] != null) {
                String extendedSentence;
                if (i == 26) {
                    extendedSentence = sentence + " ";
                } else {
                    char c = (char) (i+97);
                    extendedSentence = sentence + String.valueOf(c);
                }
                updateSentenceCounts(root.children[i], extendedSentence);
            }
        }
        
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */





//  Thought I'd optimized...about the same performance
import java.util.*;
class TrieNode {
    TrieNode[] children;
    int times;
    
    public TrieNode() {
        this.children = new TrieNode[27];
        this.times = 0;
    }
}

class AutocompleteSystem {
    TrieNode trie;
    String currentSearch;
    TrieNode currentSearchRoot;
    List<String> currentRecommendations;
    Map<String, Integer> sentenceCounts;
        
    public AutocompleteSystem(String[] sentences, int[] times) {
        this.trie = createTrie(sentences, times);
        this.currentSearch = "";
        this.currentSearchRoot = this.trie;
        this.currentRecommendations = null;
        this.sentenceCounts = new HashMap<String, Integer>();
    }
    
    public TrieNode createTrie(String[] sentences, int[] times) {
        TrieNode trie = new TrieNode();
        TrieNode root;
        int sentenceId = 0;
        for (String sentence : sentences) {
            root = trie;
            for (char c : sentence.toCharArray()) {
                int charIndex;
                if (c == ' ') {
                    charIndex = 26;
                } else {
                    charIndex = c-'a';    
                }
                
                if (root.children[charIndex] == null) {
                    root.children[charIndex] = new TrieNode();
                }
                root = root.children[charIndex];
            }
            root.times = times[sentenceId++];
        }    
        return trie;
    }
    
    public void insertSentence(String sentence) {
        TrieNode root = this.trie;
        for (char c : sentence.toCharArray()) {
            int charIndex;
            if (c == ' ') {
               charIndex = 26; 
            } else {
                charIndex = c-'a';
            }
            
            if (root.children[charIndex] == null) {
                root.children[charIndex] = new TrieNode();
            }
            root = root.children[charIndex];
        }
        root.times++;
    }
    
    
    public List<String> input(char c) {
        int cIndex = (c == ' ') ? 26 : c-'a';
        
        if (c == '#') {
            insertSentence(this.currentSearch);
            this.currentSearch = "";
            this.currentRecommendations = null;
            this.currentSearchRoot = this.trie;
            return new ArrayList<String>();
        } else if (this.currentSearchRoot.children[cIndex]==null) {
            this.currentSearch += String.valueOf(c);
            this.currentRecommendations = null;
            this.currentSearchRoot = new TrieNode();
            return this.currentRecommendations;
        } else {
            this.currentSearch += String.valueOf(c);
            this.currentSearchRoot = this.currentSearchRoot.children[cIndex];
            this.updateRecommendations();
            return this.currentRecommendations.subList(0, 3);
        }
    }
    
    public void updateRecommendations() {
        this.sentenceCounts = new HashMap<String, Integer>();
        
        if (this.currentRecommendations == null) {
            this.currentRecommendations = new ArrayList<String>();
            updateSentenceCounts(this.currentSearchRoot, "");
            
            Comparator<String> sentenceComparator = new Comparator<String>() {
                
                public int compare(String a, String b) {
                    if (sentenceCounts.getOrDefault(a, 0) != sentenceCounts.getOrDefault(b, 0)) {
                        return sentenceCounts.getOrDefault(b, 0) - sentenceCounts.getOrDefault(a, 0);
                    } else {
                        return a.compareTo(b);
                    }
                }
            };
            
            PriorityQueue<String> pq = new PriorityQueue<String>(sentenceComparator);
            for (Map.Entry<String, Integer> entry : this.sentenceCounts.entrySet()) {
                pq.offer(entry.getKey());
            }
            while (pq.size() > 0) {
                String nxt = pq.poll();
                this.currentRecommendations.add(nxt);
            }
        } else {
            String newCharacter = this.currentSearch[this.currentSearch.length()-1];
            ArrayList<String> updatedRecommendations = new ArrayList<String>();
            for (String s : this.currentRecommendations) {
                if (s[this.currentSearch.length()-1] == newCharacter) {
                    updatedRecommendations.add(s);
                }
            }
            this.currentRecommendations = updatedRecommendations;
        }
    }
    

    public void updateSentenceCounts(TrieNode root, String sentence) {        
            
        if (root.times > 0) {
            this.sentenceCounts.put(this.currentSearch + sentence, root.times);
        }
        
        for (int i = 0; i < 27; i++) {
            if (root.children[i] != null) {
                String extendedSentence;
                if (i == 26) {
                    extendedSentence = sentence + " ";
                } else {
                    char c = (char) (i+97);
                    extendedSentence = sentence + String.valueOf(c);
                }
                updateSentenceCounts(root.children[i], extendedSentence);
            }
        }
        
    }
}




// TODO: write a better solution to this

