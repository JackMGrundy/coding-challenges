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
# Built ins. 98th percentile. 
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict([])
        self.numItems = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        val = self.dict[key]
        del self.dict[key]
        self.dict[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
            return 
        
        if self.numItems == self.capacity:
            self.dict.popitem(last=False)
        else:
            self.numItems += 1
        
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Second attempt: 99th percentile...uses linked list
#Used a doubly linked list with caps of 0 on either end.
#This implementation relies on the assumption that only positive 
# keys are sent to the cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
        
class LRUCache:
    def __init__(self, capacity):
        self.cache = {} #key -> Node
        self.cap = capacity
        self.headCap = Node(0, 0)
        self.tailCap = Node(0, 0)
        self.headCap.next = self.tailCap
        self.tailCap.prev = self.headCap

        
    def get(self, key):
        if key in self.cache:
            res = self.cache[key]
            self._del(res)
            self._add(res)
            return(res.val)
        else:
            return(-1)
        
    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            self._del(node)
            node.val = val
            self.cache[key] = node
            self._add(node)
        else:
            newNode = Node(key, val)
            if len(self.cache)==self.cap:
                oldHeadKey = self.headCap.next.key
                del self.cache[oldHeadKey]
                self._del(self.headCap.next)
            self.cache[key] = newNode
            self._add(newNode)
        return()


    def _del(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev              
    
    def _add(self, node):
        oldTail = self.tailCap.prev
        oldTail.next = node
        node.prev = oldTail
        node.next = self.tailCap
        self.tailCap.prev = node