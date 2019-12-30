/*
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

// 4ms. 99th percentile. Iterative.
/**
 Definition for singly-linked list.
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(nullptr) {}
 };

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* previous = nullptr;
        ListNode* temp = nullptr;
        while(head) {
            temp = head -> next;
            head -> next = previous;
            previous = head;
            head = temp;
        }
        
        return previous;
    }
};


// 8ms. 78 percentile. recursive.
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        return helper(head, nullptr);
    }

private:
    ListNode* helper(ListNode* head, ListNode* previous) {
        if (!head) return previous;
        
        ListNode* stash = head -> next;
        head -> next = previous;
        return helper(stash, head);
    }
};

/*
Notes:

For the recursive solution:
At each level, save head's next and then make head point to the previous node instead. 
Spin up the next level. 
The stopping condition is when head is null. 
The only thing that isn't completely intuitive is the return. Note that at every level
we are returning the result of the level below it. And because the bottom level occurs
when head is null and previous is the original end (now new start) of the list, we will
ultimately return the new start of the list. 

*/