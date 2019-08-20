"""
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
"""

# 686 ms. 74th percentile
# 100th percentile is around 500ms and 50th percentile is around 820 ms
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.currentSearchRoot = self.trie
        self.currentSearchTerm = ""
        
        for i, sentence in enumerate(sentences):
            root = self.trie
            for c in list(sentence):
                if c not in root:
                    root[c] = {}
                
                root = root[c]
            root["*"] = times[i]
        

    def input(self, c: str) -> List[str]:
        if c == "#":
            root = self.trie
            for c in self.currentSearchTerm:
                if c not in root:
                    root[c] = {}
                root = root[c]
            root["*"] = (0 if "*" not in root else root["*"]) + 1
            
            self.currentSearchRoot = self.trie
            self.currentSearchTerm = ""
            return []
        elif not self.currentSearchRoot or c not in self.currentSearchRoot:
            self.currentSearchTerm += c
            self.currentSearchRoot = {}
            return []
        else:
            self.currentSearchTerm += c
            self.currentSearchRoot = self.currentSearchRoot[c]
            sentenceCounts = self.getSentenceCounts()
            res = [ x[0] for x in sentenceCounts[:3] ]
            
            return res


    
    def getSentenceCounts(self) -> dict:
        sentenceCounts = {}
        
        def helper(root, additionalLetters):
            nonlocal sentenceCounts
            
            if "*" in root:
                sentenceCounts[self.currentSearchTerm+additionalLetters] = root["*"]
            
            for c in root:
                if c != "*":
                    helper(root[c], additionalLetters+c)
            
        helper(self.currentSearchRoot, "")
        
        res = [ (sentence, sentenceCounts[sentence]) for sentence in sentenceCounts ]
        res.sort(key=lambda x: (-x[1], x[0]) )
        
        return res
    
    
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)







# 564ms 94th percentile.
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = self.createTrie(sentences, times)
        self.currentSearchRoot = self.trie
        self.currentSearchTerm = ""
        self.currentRecommendations = []

    def createTrie(self, sentences, times):
        trie = {}
        for i, sentence in enumerate(sentences):
            root = trie
            for c in list(sentence):
                if c not in root:
                    root[c] = {}
                
                root = root[c]
            root["*"] = times[i]
        return trie
    
    
    def addSentenceToTrie(self, sentence):
        root = self.trie
        for c in sentence:
            if c not in root:
                root[c] = {}
            root = root[c]
        root["*"] = (0 if "*" not in root else root["*"]) + 1
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.addSentenceToTrie(self.currentSearchTerm)
            self.currentSearchRoot = self.trie
            self.currentSearchTerm = ""
            self.currentRecommendations = []
            return []
        elif not self.currentSearchRoot or c not in self.currentSearchRoot:
            self.currentSearchTerm += c
            self.currentSearchRoot = {}
            self.currentRecommendations = []
            return self.currentRecommendations
        else:
            self.currentSearchTerm += c
            self.currentSearchRoot = self.currentSearchRoot[c]
            self.updateRecommendations()
            return self.currentRecommendations[0:3]


    def countSentences(self, trie):
        sentenceCounts = []
        def helper(root, additionalLetters):
            nonlocal sentenceCounts
            
            for c in root:
                if c == "*":
                    sentenceCounts.append( (self.currentSearchTerm + additionalLetters, root["*"]) )
                else:
                    helper(root[c], additionalLetters + c)
        
        helper(trie, "")
        return sentenceCounts
        
        
    def updateRecommendations(self):
        if self.currentRecommendations == []:
            sentenceCounts = self.countSentences(self.currentSearchRoot)
            sentenceCounts.sort(key=lambda x: (-x[1], x[0]) )
            self.currentRecommendations = [ x[0] for x in sentenceCounts ]
        else:
            newCharacter = self.currentSearchTerm[-1]   
            self.currentRecommendations = [ rec for rec in self.currentRecommendations  \
                                                        if len(rec) >= len(self.currentSearchTerm) \
                                                        and rec[len(self.currentSearchTerm)-1] == newCharacter ]
    
    
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)





# 291ms. 13th percentile.
# Thought I optimized...but I guess not...
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
            return new ArrayList<String>();
        } else {
            this.currentSearch += String.valueOf(c);
            this.currentSearchRoot = this.currentSearchRoot.children[cIndex];
            this.updateRecommendations();
            int numRecsAvailable = Math.min(3, this.currentRecommendations.size());
            return this.currentRecommendations.subList(0, numRecsAvailable);
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
            char newCharacter = this.currentSearch.charAt(this.currentSearch.length()-1);
            ArrayList<String> updatedRecommendations = new ArrayList<String>();
            for (String s : this.currentRecommendations) {
                
                if (s.length() >= this.currentSearch.length() &&
                    s.charAt(this.currentSearch.length()-1) == newCharacter) {
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











# Optimized
import java.util.*;
class TrieNode {
    TrieNode[] children;
    int times;
    
    public TrieNode() {
        this.children = new TrieNode[256];
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
                charIndex = c-'a';    
                
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
            charIndex = c-'a';
            
            if (root.children[charIndex] == null) {
                root.children[charIndex] = new TrieNode();
            }
            root = root.children[charIndex];
        }
        root.times++;
    }
    
    
    public List<String> input(char c) {
        int cIndex = c-'a';
        
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
            return new ArrayList<String>();
        } else {
            this.currentSearch += String.valueOf(c);
            this.currentSearchRoot = this.currentSearchRoot.children[cIndex];
            this.updateRecommendations();
            int numRecsAvailable = Math.min(3, this.currentRecommendations.size());
            return this.currentRecommendations.subList(0, numRecsAvailable);
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
            char newCharacter = this.currentSearch.charAt(this.currentSearch.length()-1);
            ArrayList<String> updatedRecommendations = new ArrayList<String>();
            for (String s : this.currentRecommendations) {
                
                if (s.length() >= this.currentSearch.length() &&
                    s.charAt(this.currentSearch.length()-1) == newCharacter) {
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
                char c = (char) (i+97);
                extendedSentence = sentence + String.valueOf(c);
                }
                updateSentenceCounts(root.children[i], extendedSentence);
            }
        }
        
    }
}