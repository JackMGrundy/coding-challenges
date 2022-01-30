/*
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
*/

// 79th percentile
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == p || root == q || !root) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if (left && right) return root;
        else if (!left) return right;
        else return left;
    }
};



/*

The LCA is the node that has one node in its left subtree and the other in its right
OR that equals one of the two nodes and has the other as a child...

This means that at each node, in order to determine if it's the LCA, we need to know
if the target nodes are in its subtrees.

What kind of traversal do we need for this? Post order dfs...
that starts at the bottom of the tree and then works up...

we can add a tiny tweak...if we hit a node that is one of the two, we can just return it...
if it's the case that the node is the LCA (meaning the other node is in a subtree), we don't
care about finding the other node...

setting that aside, it's just standard post order traversal...you make a call to visit the left
tree first, then the right tree, and then we "visit the node"...
intuitively the left call is going all the way down the left side of the tree before we do any work
and before any parent node (the second to lowest level) does any work, it will have data on its two subtrees

Algorithm Postorder(tree)
   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
   3. Visit the root.
*/