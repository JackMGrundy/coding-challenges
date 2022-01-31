/*
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.
*/


// 63rd percentile
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        int pDepth = depth(p);
        int qDepth = depth(q);
        
        while (pDepth < qDepth) {
            q = q->parent;
            qDepth--;
        }
        
        while (qDepth < pDepth) {
            p = p->parent;
            pDepth--;
        }
        
        while (p != q) {
            p = p->parent;
            q = q->parent;
        }
        
        return p;
    }

    private:
    int depth(Node* node) const {
        int nodeDepth = 0;
        while (node->parent) {
            node = node->parent;
            nodeDepth++;
        }
        
        return nodeDepth;
    }
};


// 80th percentile
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        Node* pRunner = p;
        Node* qRunner = q;
        while (pRunner != qRunner) {
            if (pRunner)
                pRunner = pRunner->parent;
            else
                pRunner = p;
            
            if (qRunner)
                qRunner = qRunner->parent;
            else
                qRunner = q;
        }
        
        return pRunner;
    }
};

/*
Last one uses the same idea as finding the convergence of two linked lists
*/