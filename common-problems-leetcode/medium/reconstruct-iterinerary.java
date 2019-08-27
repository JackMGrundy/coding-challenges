/*
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
*/

// Slow Java solution...copying logic verbatim from python
// 9ms. 35th percentile. Iterative.
// 6ms gets you to ~80th percentile. I can live with 3ms in this case.
import java.util.*;
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, List> targets = new HashMap<String, List>();
        
        for(List<String> ls : tickets) {
            String a = ls.get(0);
            String b = ls.get(1);
            List<String> list = targets.getOrDefault(a, new ArrayList<String>());
            list.add(b);
            targets.put(a, list);
        }
        
        for (Map.Entry<String, List> entry : targets.entrySet()) {
            Collections.sort(entry.getValue());
        }
        
        Stack<String> stack = new Stack<String>();
        stack.push("JFK");
        List<String> path = new ArrayList<String>();
        while (stack.size() > 0) {
            while (targets.containsKey(stack.peek()) && targets.get(stack.peek()).size() > 0) {
                List<String> curTargets = targets.get(stack.peek());
                stack.push( curTargets.remove( 0 ));
            }
            path.add(stack.pop());
        }
        Collections.reverse(path);
        return path;
    }
}



// Cleaner using priority queue and computeIfAbsent. Iterative. 
// Crazy Slow. Only ~2 times faster than Python..38ms.
import java.util.*;
class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, PriorityQueue<String>> targets = new HashMap<String, PriorityQueue<String>>();
        for (List<String> ticket : tickets) {
            targets.computeIfAbsent(ticket.get(0), k -> new PriorityQueue<String>()).add(ticket.get(1));
        }
        
        Stack<String> stack = new Stack<String>();
        stack.push("JFK");
        List<String> path = new ArrayList<String>();
        while (!stack.isEmpty()) {
            while (targets.containsKey(stack.peek()) && !targets.get(stack.peek()).isEmpty()) {
                stack.push( targets.get(stack.peek()).poll() );
            }
            path.add(stack.pop());
        }
        Collections.reverse(path);
        return path;
    }
}



// Recursive. 35ms. 24th percentile. Also slower.
import java.util.*;
class Solution {
    Map<String, PriorityQueue<String>> targets = new HashMap<String, PriorityQueue<String>>();
    List<String> path = new ArrayList<String>();
    
    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> ticket : tickets) {
            targets.computeIfAbsent(ticket.get(0), k -> new PriorityQueue<String>()).add(ticket.get(1));
        }
        
        visit("JFK");
        Collections.reverse(path);
        return path;
    }
    
    void visit(String destination) {
        while (targets.containsKey(destination) && !targets.get(destination).isEmpty()) {
            visit( targets.get(destination).poll() );
        }
        path.add(destination);
    }
}