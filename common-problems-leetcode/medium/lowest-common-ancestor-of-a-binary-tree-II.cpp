/*
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
 

Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
*/



// 28th percentile
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
        TreeNode* ans = helper(root, p, q);
        return (pFound && qFound) ? ans: NULL;
    }

private:
    TreeNode* helper(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return root;
        
        TreeNode* left = helper(root->left, p, q);
        TreeNode* right =  helper(root->right, p, q);
        if (root == p) {
            pFound = true;
            return root;
        }
        if (root == q) {
            qFound = true;
            return root;
        }
        
        return !left ? right : !right ? left : root;
    }
    
    bool qFound = false;
    bool pFound = false;
};

// 65th percentile
// Skip some searching if possible
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        helper(root, p, q);
        return answer;
    }

private:
    int helper(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) 
            return 0;
        int found = (root == p || root == q) ? 1 : 0;
        found += helper(root->left, p, q);
        if (found < 2)
            found += helper(root->right, p, q);
        
        if (found == 2 && !answer) 
            answer = root;
        
        return found;
    }
    
    TreeNode* answer = nullptr;
};

// 95th percentile
// Refactor: note the capture expression and the recursive lamdba
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* LCA = nullptr;
        std::function<int(TreeNode* root)> dfs = [&LCA, &p, &q, &dfs](TreeNode* root) {
            if (!root)
                return 0;
            int found = (root == p || root == q) ? 1 : 0;
            found += dfs(root->left);
            if (found < 2)
                found += dfs(root->right);
            if (found == 2 && !LCA)
                LCA = root;
            return found;
        };
        dfs(root);
        return LCA;
    }
};


// 95th percentile
// refactor - notice the [&] for getting references to all outside variables
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* LCA = nullptr;
        std::function<int(TreeNode* root)> dfs = [&](TreeNode* root) {
            if (!root)
                return 0;
            int found = (root == p || root == q) ? 1 : 0;
            found += dfs(root->left);
            if (found < 2)
                found += dfs(root->right);
            if (found == 2 && !LCA)
                LCA = root;
            return found;
        };
        dfs(root);
        return LCA;
    }
};