/*
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
*/
// 124ms. 5th percentile.
class Trie {
    HashMap<String, HashMap> trie;
    
    /** Initialize your data structure here. */
    public Trie() {
        this.trie = new HashMap<String, HashMap>();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        HashMap<String, HashMap> root = this.trie;
        for (String c : word.split("")) {
            if (root.containsKey(c)) {
                root = root.get(c);
            } else {
                HashMap<String, HashMap> temp = new HashMap<String, HashMap>();
                root.put(c, temp);
                root = root.get(c);
            }
        }
        root.put("#", null);
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        HashMap<String, HashMap> root = this.trie;
        for (String c : word.split("")) {
            if (root.containsKey(c)) {
                root = root.get(c);
            } else {
                return false;
            }
        }
        return root.containsKey("#");
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        HashMap<String, HashMap> root = this.trie;
        for (String c : prefix.split("")) {
            if (root.containsKey(c)) {
                root = root.get(c);
            } else {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */




 


//  74ms. 87th percentile.
class TrieNode {
    TrieNode[] children;
    String word;
        
    public TrieNode() {
        this.children = new TrieNode[26];
        this.word = null;
    }
}


class Trie {
    TrieNode root;
    
    /** Initialize your data structure here. */
    public Trie() {
        this.root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode currentNode = this.root;
        for (char c : word.toCharArray()) {
            int charIndex = c-'a';
            if (currentNode.children[charIndex] == null) {
                currentNode.children[charIndex] = new TrieNode();
            } 
            currentNode = currentNode.children[charIndex];
        }
        currentNode.word = word;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode currentNode = this.root;
        for (char c : word.toCharArray()) {
            int charIndex = c-'a';
            if (currentNode.children[charIndex] == null) {
                return false;
            } else {
                currentNode = currentNode.children[charIndex];
            }
        }
        
        return currentNode.word != null;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode currentNode = this.root;
        for (char c : prefix.toCharArray()) {
            int charIndex = c-'a';
            if (currentNode.children[charIndex] == null) {
                return false;
            } else {
                currentNode = currentNode.children[charIndex];
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */