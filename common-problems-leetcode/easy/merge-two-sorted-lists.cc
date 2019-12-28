/*
"""
Merge two sorted linked lists and return it as a new list. The new 
list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
*/

// 4ms. 99th percentile. 
#include <string>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(-1);
        ListNode* linker = &head;
        
        while (l1 && l2) {
            if (l1->val <= l2-> val) {
                linker->next = l1;
                l1 = l1->next;
            } else {
                linker->next = l2;
                l2 = l2->next;
            }
            linker = linker->next;
        }
        
        linker->next = l1 ? l1 : l2;
        return head.next;
    }
};

/*
Notes:

Note the use of ->
Linker is a point to the head list node at the start. Linker is not itself
a list node, so we can't do something like linker.val. -> is equivalent to 
dereferencing linker and then accessing an attribute. 

a->b means (*a).b

*/