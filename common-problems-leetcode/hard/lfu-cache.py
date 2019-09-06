"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# 224ms. 96th percentile.
class LFUCache:

    def __init__(self, capacity: int):
        self.keyToValue = {}
        self.keyToFrequency = {}
        self.frequencyLists = {}
        self.capacity = capacity
        self.minFrequency = 1

    def get(self, key: int) -> int:       
        if key not in self.keyToValue:
            return -1
        
        keyFrequency = self.keyToFrequency[key]
        del self.frequencyLists[keyFrequency][key]
        
        updatedValFrequency = keyFrequency+1
        if updatedValFrequency not in self.frequencyLists:
             self.frequencyLists[updatedValFrequency] = collections.OrderedDict([])
        self.frequencyLists[updatedValFrequency][key] = None
        self.keyToFrequency[key] = updatedValFrequency
        
        if len(self.frequencyLists[keyFrequency])==0 and keyFrequency == self.minFrequency:
            self.minFrequency += 1

        return self.keyToValue[key]
        
    
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.keyToValue:
            self.keyToValue[key] = value
            self.get(key)
            return
        
        if len(self.keyToValue) >= self.capacity:
            popKey, popValue = self.frequencyLists[self.minFrequency].popitem(last=False)
            del self.keyToValue[popKey]
            del self.keyToFrequency[popKey]
        
        self.keyToValue[key] = value
        self.keyToFrequency[key] = 1
        self.minFrequency = 1
        if 1 not in self.frequencyLists:
            self.frequencyLists[1] = collections.OrderedDict([])
        self.frequencyLists[1][key] = None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
Notes

Simple in concept...devil is in the implementation

Instance variables
key -> value
key -> frequency
frequency -> list of keys with that frequency (use an ordered list so we can easily get the first 
        inserted aka least recently used element)
capacity
the min frequency so far


Get:
    If we don't have key, return -1
    Otherwise, get the old frequency and delete the element from its old frequency list

    If the old frequency was the min frequency and there are no more elements in that
    frequency list, delete the old frequency list.

    Increment the key's frequency 
    Check if a list currently exists for that frequency. If not, make one. 
    Add the key to this frequency list. 

    Update the keyTofrequency map

    Finally return the value


Put:
    Handle the edge case of a 0-capacity cache (hmmm)

    If the cache already has the key, update the value. Then call get on the key. This
    is an easy way to quickly update the frequency for that key. In a more complete
    implementation, we might want to refactor out that logic. 

    Else:
        If we're at capacity, pop the least recently used element from the min frequnecy list.
        Delete that element fom the keyToValue map and the keyToFrequency map.

        Insert the new key/value pair into the keyToValue map
        Set the keyToFrequency for the key to just 1 (it's a new element)
        We can set the minFrequency to 1 now
        If we don't have a frequency 1 frequencyList, create one.
        And add the new element to that frequency list

Implementation note: Python doesn't have an ordered set like Java's LinkedHashSet, so just
use an Ordered Dict.  
"""