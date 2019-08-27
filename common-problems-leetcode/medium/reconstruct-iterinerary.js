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

// 88ms. 41 percentile.
/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    let targets = {};
    tickets.sort( (a,b) => {
        if (b[0] !== a[0]) {
            return b[0].localeCompare(a[0]);
        } else {
            return b[1].localeCompare(a[1]);
        }
    });
    
    for (let ticket of tickets) {
        let a = ticket[0];
        let b = ticket[1];
        targets[a] = a in targets ? targets[a].concat([b]) : [b];
    }
    
    let res = [];
    let stack = ["JFK"];
    while (stack.length > 0) {
        while (stack[stack.length-1] in targets && targets[stack[stack.length-1]].length > 0) {
            stack.push(targets[stack[stack.length-1]].pop());
        }
        res.push( stack.pop() );
    }
    res.reverse();
    return res;
};


// 88ms. 41 percentile. recursive.
/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    let targets = {};
    tickets.sort( (a,b) => {
        if (b[0] !== a[0]) {
            return b[0].localeCompare(a[0]);
        } else {
            return b[1].localeCompare(a[1]);
        }
    });
    
    for (let ticket of tickets) {
        let a = ticket[0];
        let b = ticket[1];
        targets[a] = a in targets ? targets[a].concat([b]) : [b];
    }
    
    let res = [];
    let visit = function(destination) {
        while (destination in targets && targets[destination].length > 0) {
            visit(targets[destination].pop());
        }
        res.push(destination);
    }
    visit("JFK");
    res.reverse();
    return res;
};