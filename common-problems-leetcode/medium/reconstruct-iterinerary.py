"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

"""
Fascinating little problem. So per usual with DFS, it's nice that when you hit a deadend, you 
can double back to try going down a different path. There's a twist with this problem. We know up front 
that every ticket will be used. Further, we know that the last destination is just that, a final destination. 
More formally, the only noes with odd degrees are the entrance and the exit (unless the start and end are the
same node...then they're all even). Just think through a few examples...
So the "dead end" isn't a dead end here...it tells us where the end of the list is. So we can add that to our route...
we do this for every target and then reverse at the end. 

"""
# 88ms. 86th percentile. Iterative.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        stack = ["JFK"]
        res = []
        while stack:
            while targets[stack[-1]]:
                stack.append( targets[stack[-1]].pop() )
            res.append(stack.pop())
        return res[::-1]

# Recursive. 86 percentile. 88ms
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            targets[a].append(b)
        res = []
        def hop(destination):
            while targets[destination]:
                hop(targets[destination].pop())
            res.append(destination)
        hop("JFK")
        return res[::-1]