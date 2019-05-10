"""
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
"""
# 39th percentile
"""
Dynamic resizing. Chaining. Multiplication hashing.
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tableSize = 8
        self.load = 0
        self.doublingThreshold = 0.7
        self.table = [ [] for _ in range(self.tableSize) ]
        self.hashConstant = (5 **.5  - 1.0)/2.0

    def hashKey(self, key):
        return math.floor( self.tableSize * ( (self.hashConstant * key) % 1 ) )
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        slot = self.hashKey(key)
        newNode = (key, value)
        
        # Update element
        for i, ele in enumerate(self.table[slot]):
            eleKey, eleValue = ele
            if eleKey == key:
                self.table[slot][i] = newNode
                return
        
        # Add new element
        self.table[slot].append(newNode)
        self.load += 1.0
        
        # Resize table
        if float(self.load) / self.tableSize >= self.doublingThreshold:
            self.tableSize *= 2
            biggerTable = [ [] for _ in range(self.tableSize) ]
            for slot in self.table:
                for ele in slot:
                    key, value = ele
                    eleNewSlot = self.hashKey(key)
                    biggerTable[eleNewSlot].append( (key, value) )
            
            self.table = biggerTable
        
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        slot = self.hashKey(key)
        for ele in self.table[slot]:
            eleKey, eleValue = ele
            if key == eleKey:
                return eleValue
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        slot = self.hashKey(key)
        for i, ele in enumerate(self.table[slot]):
            eleKey, eleValue = ele
            if key == eleKey:
                del self.table[slot][i]
                return
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# 83rd percentile
"""
Fixed table size of 1000. Chaining. This implementation is not production
grade, because it is absolutely dependent on a limited number of elements being hashed in.
It's faster for this challenge though, because it is optimized for these test cases. 
"""
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tableSize = 1000
        self.table = [ [] for _ in range(self.tableSize)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        slot = key % self.tableSize
        newEle = (key, value)
        
        # Update
        for i, ele in enumerate(self.table[slot]):
            eleKey, eleVal = ele
            if eleKey == key:
                self.table[slot][i] = newEle
                return
        
        # New
        self.table[slot].append( newEle )
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        slot = key % self.tableSize
        for ele in self.table[slot]:
            eleKey, eleVal = ele
            if eleKey == key:
                return eleVal
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        slot = key % self.tableSize
        for i, ele in enumerate(self.table[slot]):
            eleKey, eleVal = ele
            if eleKey == key:
                del self.table[slot][i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)