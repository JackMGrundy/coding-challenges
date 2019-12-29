/*
A linked list is given such that each node contains an additional random pointer which could 
point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
*/

// 1st attempt. recursive. 1ms 73rd percentile in speed...doesn't mean much because
// everyone got 1ms. 
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/

// 8ms. 99th percentile.
#include <unordered_map>

class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};


class Solution {
std::unordered_map<Node*, Node*> map;

public:
    Node* copyRandomList(Node* head) {
        if (!head) {
            return nullptr;
        }
        
        if (map.find(head) != map.end()) {
            return map[head];
        }

        Node* copy = new Node(head->val);
        map[head] = copy;
        copy->next = copyRandomList(head->next);
        copy->random = copyRandomList(head->random);
        return copy;
    }
};