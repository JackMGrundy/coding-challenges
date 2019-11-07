/* 

We  are given a binary tree (with root node root), a target node, and an integer
value K.                                                                        

Return  a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.                                 

                                                                                

Example 1:                                                                      

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2                  

Output: [7,4,1]                                                                 

Explanation:                                                                    

The nodes that are a distance 2 from the target node (with value 5)             

have values 7, 4, and 1.                                                        

Note that the inputs "root" and "target" are actually TreeNodes.                

The descriptions of the inputs above are just serializations of these objects.  

                                                                                

Note:                                                                           

The given tree is non-empty.                                                    

Each node in the tree has unique values 0 <= node.val <= 500.                   

The target node is a node in the tree.                                          

0 <= K <= 1000.                                                                 



*/


// 4ms. 26 percentile.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Tuple {
    TreeNode node;
    int distance;
    
    public Tuple(TreeNode node, int distance) {
        this.node = node;
        this.distance = distance;
    }
}

class Solution {
    Map<TreeNode, TreeNode> parents;
    TreeNode start;
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        parents = new HashMap();
        dfs(root, null, target);
        
        Queue<Tuple> queue = new LinkedList();
        Tuple rootTuple = new Tuple(start, 0);
        queue.offer(rootTuple);
        
        TreeNode currentNode;
        Tuple current, left, right, parent;
        
        Set <TreeNode> seen = new HashSet();
        
        List<Integer> result = new ArrayList<Integer>();
        
        while (!queue.isEmpty()) {
            current = queue.poll();
            
            if (current.node == null || seen.contains(current.node) || K < current.distance) {
                continue;
            }
            seen.add(current.node);
            
            if (K == current.distance) {
                result.add(current.node.val);
                continue;
            }
            else {
                left = new Tuple(current.node.left, current.distance + 1);
                right = new Tuple(current.node.right, current.distance + 1);
                parent = new Tuple( parents.get(current.node), current.distance + 1);
                
                queue.offer(left);
                queue.offer(right);
                queue.offer(parent);
            }
        }
        
        return result;
    }
    
    
    public void dfs(TreeNode root, TreeNode parent, TreeNode target) {
        if (root != null) {
            if (start == null && root == target) {
                start = root;
            }
            
            parents.put(root, parent);
            dfs(root.left, root, target);
            dfs(root.right, root, target);
        }
        
    }
}




/*

Notes:

Easiest method I can think of is to create a mapping from children to parents. Given this,
you can just do a bfs out from the target node. 

*/