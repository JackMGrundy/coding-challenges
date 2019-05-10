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
// 93rd percentile
/*
Fixed table size. Chaining. Not a robust solution. Good for an interview question that specifies a limited 
number of elements will be hashed and that there is a fixed range of keys.
*/
/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
    this.tableSize = 1000;
    this.table = new Array(this.tableSize).fill(0).map( arr => new Array());
};

MyHashMap.prototype.hash = function(key) {
    return key % this.tableSize
}

/**
 * value will always be non-negative. 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    let slot = this.hash(key);
    
    // Update
    for (let i = 0; i < this.table[slot].length; i++) {
        let {eleKey, eleValue} = this.table[slot][i];
        if (eleKey === key) {
            this.table[slot][i] = { eleKey : key, eleValue: value };
            return;
        }
    }
    
    // New ele
    this.table[slot].push( { eleKey: key, eleValue: value} );
    return

};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    let slot = this.hash(key);
    
    for (let i = 0; i < this.table[slot].length; i++) {
        let {eleKey, eleValue} = this.table[slot][i];
        if (eleKey === key) {
            return eleValue
        }
    }
    return -1;
};


/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    let slot = this.hash(key);
    
    for (let i = 0; i < this.table[slot].length; i++) {
        let {eleKey, eleValue} = this.table[slot][i];
        if (eleKey === key) {
            this.table[slot].splice(i, 1);
            return;
        }
    }
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */



 

//  69th percentile. 228ms.
/*
Although it performs slower on these tests, I think this is a much better solution. Dynamic resizing.
Chaining. Multiplication hashing. 
*/
/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
    this.tableSize = 8;
    this.doublingFactor = 0.7;
    this.table = new Array(this.tableSize).fill(0).map(arr => new Array());
    this.load = 0;
    this.hashingConstant = (5 ** 0.5 - 1) / 2 // golden ratio
};

MyHashMap.prototype.hash = function(key) {
    return Math.floor(this.tableSize * ( (this.hashingConstant * key) % 1 ) )
}

/**
 * value will always be non-negative. 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    let slot = this.hash(key);
    
    // Update
    for (let i = 0; i < this.table[slot].length; i++) {
        let { eleKey, eleValue } = this.table[slot][i];
        if (eleKey === key) {
            this.table[slot][i] = { eleKey: key, eleValue: value };
            return
        }
    }
    
    // New element
    this.table[slot].push( { eleKey : key, eleValue : value } );
    this.load++;
    
    // Resize table if needed
    if ( parseFloat(this.load) / this.tableSize > this.doublingFactor ) {
        this.tableSize *= 2;
        let biggerTable = new Array(this.tableSize).fill(0).map(arr => new Array());
        for (let slot = 0; slot < this.table.length; slot++) {
            for (let ele = 0; ele < this.table[slot].length; ele++) {
                let { eleKey, eleValue } = this.table[slot][ele];
                let newSlot = this.hash(eleKey);
                biggerTable[newSlot].push( { eleKey: eleKey, eleValue: eleValue } );
            }
        }
        this.table = biggerTable;
    }
    return;
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    let slot = this.hash(key);
    
    for (let ele = 0; ele < this.table[slot].length; ele++) {
        let { eleKey, eleValue } = this.table[slot][ele];
        if (eleKey === key) {
            return eleValue;
        }
    }
    return -1;
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    let slot = this.hash(key);
    
    for (let ele = 0; ele < this.table[slot].length; ele++) {
        let { eleKey, eleValue } = this.table[slot][ele];
        if (eleKey === key) {
            this.table[slot].splice(ele, 1);
            this.load--;
            return;
        }
    }
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */