"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Brute force. Nlog(N). N space. N = total number of nodes
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nums = []
        for l in lists:
            while l:
                nums.append(l.val)
                l = l.next
            
        head = runner = ListNode(0)
        for num in sorted(nums):
            runner.next = ListNode(num)
            runner = runner.next

        return head.next


# Simple priority queue approach. 100ms. 98 percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [ ls for ls in lists if ls != None ]
        if not lists:
            return None

        pq = []
        for i,head in enumerate(lists):
            heappush(pq, (head.val, i, head))
        
        cap = merger = ListNode(-1)
        while pq:
            _, i, node = heappop(pq)
            if node.next:
                heappush(pq, (node.next.val, i, node.next))
            merger.next = node
            merger = merger.next
        
        return cap.next


# Merge in one list at a time. O(N)K time where N is total nodes
# and k is number of lists.
# 5332ms. 7th percentile.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        head = self._mergeTwoLists(lists[0], lists[1])
        for listHead in lists[2:]:
            head = self._mergeTwoLists(head, listHead)
        
        return head
    
    
    def _mergeTwoLists(self, first, second):
        head = merger = ListNode(-1)
        
        while first or second:
            if first and not second:
                merger.next = first
                break
            elif second and not first:
                merger.next = second
                break
            elif first.val <= second.val:
                merger.next = first
                first = first.next
            elif second.val < first.val:
                merger.next = second
                second = second.next
            
            merger = merger.next
        
        return head.next


# Improve the merge in one list at a time approach with divide
# and conquer. Gives O(Nlog(K)) time and constant space
# 128ms. 53rd percentile.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        # Method 1:
        """ 
        Cool idea...we're merging 0-1, 2-3, 4-5, 6-7,....
        Then 0-2, 4-6
        Then 0-4
        So rather than make new lists, we keep merging the second lists into the 
        firsts. At the end lists[0] has the final result.
        """
        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval*2):
                lists[i] = self._mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2


        """
        A cleaner way to do the above. It overwrites the lists though. 
        """
        # while 1 < len(lists):
            # lists = [ self._mergeTwoLists(*lists[i:i+2]) for i in range(0, len(lists), 2)  ]
        
        return lists[0]
    
    
    def _mergeTwoLists(self, first, second=None):
        head = merger = ListNode(-1)
        
        while first or second:
            if first and not second:
                merger.next = first
                break
            elif second and not first:
                merger.next = second
                break
            elif first.val <= second.val:
                merger.next = first
                first = first.next
            elif second.val < first.val:
                merger.next = second
                second = second.next
            
            merger = merger.next
        
        return head.next


"""
Notes:

There are a lot of ways to do this problem.

1) Easiest is brute force. Just combine all the values into a single list
sort it and then produce a list using that list of numbers. 

2) March through the lists. At each step, compare the nodes at the front of 
the k lists. Take the smallest one. This requires NK work where K is the number of lists
and N is the total number of nodes. 

It takes N space if you make a new list. O(1) space if you just interleave the nodes


3) Same as two except for the comparisons use a prioirty queue. The comparison cost
drops to log(K), so Nlog(K) total. 
New linked list -> N space
Combine the lists -> K space (priority queue will have K elements in it at any one time)


4) This is the best approach in that its Nlog(k) but constant space. It's a bit trickier though.
The idea is cool though. In my opinion it's another example of how merge sort esque techniques
work surprisingly well with linked lists. 

At the core, we maintain a final list and merge in one list at a time. Then we do this with
a divide and conquer approach. Details:

First, note that merging two sorted linked lists is straightforwards. It's easy to imagine
just merging in a list at a time. We do this k times and process O(N) nodes in total. Total
time complexity is O(KN). Space complexity is O(1) if we merge the lists rather than
make a new one.

Now bring in the divide and conquer bit. Idea is to pair up the lists, merge the pairs, then
merge the resulting lists and so on.

This is Nlog(k) time complexity. To see why, imagine

4 lists, each with 16 elements. 

We merge them into two lists of 16 elements.

Then merge those into one list of 32 elements. 

The number of merge operations is equal to Log2(K). Each of these merges takes at
most O(N) time. So log2(K)*N space.

^Cool aside about this method is the indexing used in repeatedly merging in the lists
"""