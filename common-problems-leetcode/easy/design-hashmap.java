/*
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
Accepted
30,316
Submissions
54,385
*/
// 97th percentile. 63ms.
/*
Chaining. Fixed table size. Fixed key range. Not robust or adaptable...but fast for this problem.
*/
class MyHashMap {
    public ListNode[] table;
    public int tableSize;
    
    public int hash(int key) {
        return key % this.tableSize;
    }
    
    /** Initialize your data structure here. */
    public MyHashMap() {
        this.tableSize = 1000;
        this.table = new ListNode[this.tableSize];
        // Arrays.fill(table, 0, this.tableSize, new ListNode(-1, -1));
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        int slot = this.hash(key);
        
        // Update
        ListNode node = this.table[slot];
        while (node != null) {
            if (node.key == key) {
                node.value = value;
                return;
            }
            
            if (node.next == null) {
                break;
            }
            
            node = node.next;
        }
        
        // Add new element
        if (node == null) {
            this.table[slot] = new ListNode(key, value);
        } else {
            node.next = new ListNode(key, value);
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int slot = this.hash(key);
        
        ListNode node = this.table[slot];
        while (node != null) {
            if (node.key == key) {
                return node.value;
            }
            node = node.next;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int slot = this.hash(key);
        
        
        ListNode node = this.table[slot];
        // System.out.println(node);
        // System.out.println(key);
        // System.out.println(node.key);
        // empty chain
        if (node == null) {
            return;
        }
        // first node is target
        if (node.key == key) {
            // System.out.println(node);
            // System.out.println(node.next);
            
            this.table[slot] = node.next;
            
            // System.out.println(Arrays.toString(this.table));
            return;
        }
        // search in chain for target
        while (node != null) {
            
            if (node.next != null && node.next.key==key) {
                node.next = node.next.next;
                break;
            }
            node = node.next;
        }
    }
    
    
    class ListNode {
        int key, value;
        ListNode next;
        
        ListNode(int key, int value) {
            this.key = key;
            this.value = value;
            this.next = null;
        }
        
        public String toString() {
            return "(" + this.key + ", " + this.value + ") {" + this.next + "}";
        }
    }
}


/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */