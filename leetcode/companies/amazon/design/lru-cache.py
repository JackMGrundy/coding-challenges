"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
# First attempt: 65% percentile in speed...uses built in data structures
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.size = 0
        self.capacity = capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache: 
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return(value)
        else: 
            return(-1)
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache: 
            del self.cache[key]
            self.cache[key] = value
        else:
            if self.size >= self.capacity:
                self.cache.popitem(last=False)
                self.size -= 1
            self.cache[key] = value
            self.size += 1
        return()


# Second attempt: ___percentile...uses linked list
