/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the 
following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
*/

#include <list>
#include <unordered_map>
#include <utility>

// 112ms. 71st percentile.
// Iterator based solution
class LRUCache {
public:
    LRUCache(int capacity) : _capacity(capacity) {}
    // LRUCache(int capacity) {
    //     _capacity = capacity; 
    // }

    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        touch(it);
        return it -> second.first;
    }
    
    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            touch(it);
        }
        else {
            if (cache.size() == _capacity) {
                cache.erase(order.back());
                order.pop_back();
            }
            order.push_front(key);
        }
        cache[key] = { value, order.begin() };
    }

private:
    typedef std::list<int> LI;
    typedef std::pair<int, LI::iterator> PI;
    typedef std::unordered_map<int, PI> HPPI;
    
    HPPI cache;
    LI order;
    int _capacity;
    
    void touch(HPPI::iterator it) {
        int key = it -> first;
        order.erase(it -> second.second);
        order.push_front(key);
        it -> second.second = order.begin();
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */


/*

Notes:

Note the use of typedefs to build up a type that would otherwise be obnoxious to write
and the later used of auto to also avoiding writing it out. 

Note the use of the colon initialization list in the constructor

We could come up with a pointer based solution...a pro of using iterators is that they
make it very clear what their purpose is...i.e to point to ___ data structure.


Iterator solution: 
We use a simple list of ints to record the order in which keys have been seen. 
Newest keys at the front and oldest keys at the back. 

We have an unordered map that maps key -> pair(value, list::iterator)
...the list iterators point to the location in the list where the key is contained. 

Say we update the value for a key that is already contained...then we need to update
the location of the key in the order list. Touch does that. It takes in a key, pair(value, list::iterator)...
we can get the key from that and the location of the key in the list using the iterator...
we delete the old key in the list, add the key to the start of the list, and then update the iterator from 
the map to point to that new location. 

get and put are pretty straightforwards. Get returns -1 if we can't find the target...otherwise run touch
to update the order...at the end use the map to get the <value, list::iterator> pair needed and then return
that value

Put is also straightfoward with the one notable bit being the logic to ensure we don't exceed capacity. 

*/