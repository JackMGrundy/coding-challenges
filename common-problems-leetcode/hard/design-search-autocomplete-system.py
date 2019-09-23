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


"""
Notes:

Of course, we use a trie. 

In this design, we divide responsibility for creating the trie and maintaining it (add a new sentence)
into two different functions. These are pretty standard. The one thing to note is that the problem specifics
that # is an end sentence character - this makes it a natural place to store a sentence count in the trie...
i.e. trie["#"] = sentence count.

The primary function is input. There are three cases:
1) The user has finished inputting (we see "#"). In that case, we can add the sentence to the trie
(or increase the count if it is already in there) and update everything else that needs to be ready
for the next query. 
2) Next case...there are no recommendations for the current query. This could have already been the
case due to previous characters, or it could be due to a new character. Either way we update the current 
query with the new char (so we can insert it into the trie when the query ends), and we keep the 
recommendations and searchRoot empty.
3) We have a currently running query and we're adding a new char. In this case, we update the root
of the trie, update our recommendations based on the new char, and return recommendations.


As for the actual recommendations...
First we need a way to get all the sentences and their counts. For this its a simple backtracking
traversal over the tree. We end up with [ (sentence, count), (sentence, count) ]...

Then for the recs...
Basically, when we start a query (as indicated by the recommendations being []), we use our method
to get sentence counts. Then, for each additional character, we just filter this initial list. This
allows us to avoid traversing the trie for every set of recommendations. 


"""