/*
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

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
class Solution {
    public Map<Node, Node> copied;
    
    public Solution() {
        this.copied = new HashMap<Node, Node>();
    }
    
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        if (this.copied.containsKey(head)) {
            return this.copied.get(head);
        }
        else {
            Node newNode = new Node(head.val, null, null);
            this.copied.put(head, newNode);
            newNode.next = copyRandomList(head.next);
            newNode.random = copyRandomList(head.random);
            
            return newNode;
        }
    }
}




// 2nd attempt: iterative. 1ms 73rd percentile in speed.
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
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        Node res = new Node(head.val, head.next, head.random);
        Node normalLinker = res;
        Node randomLinker = res;
        Map<Node, Node> memo = new HashMap<Node, Node>();
        memo.put(head, res);
        
        while (head.next != null) {
            Node newNode = new Node(head.next.val, head.next.next, head.next.random);
            normalLinker.next = newNode;
            memo.put(head.next, newNode);
            
            head = head.next;
            normalLinker = normalLinker.next;
        }
        
        while (randomLinker != null) {
            if (randomLinker.random != null) {
                randomLinker.random = memo.get(randomLinker.random);
            }
            randomLinker = randomLinker.next;
        }
        
        return res;
    }
}
