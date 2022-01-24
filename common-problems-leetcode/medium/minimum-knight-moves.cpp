/*
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 
 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300
*/

// #include <pair>;
#include <vector>
#include <queue>
#include <set>
#include <unordered_set>


// 44th percentile
class Solution {
public:
    typedef std::pair<int, int> LOC;
    typedef std::pair<LOC, int> LOC_MOVE;
    
    std::vector<std::pair<int,int> > moves = { {1, 2}, {-1, 2}, {-1, -2}, {1, -2}, {2, 1}, {-2, 1}, {-2, -1}, {2, -1} };
    
    int minKnightMoves(int x, int y) {
        if (x == 0 && y == 0) return 0;
        
        std::queue<LOC_MOVE> q;
        std::set<LOC> visited;
        
        const LOC startSpot = {0, 0};   
        const LOC_MOVE startSpotAndMove = { startSpot, 0 };
        q.push(startSpotAndMove);
        visited.insert(startSpot);
        
        x = std::abs(x);
        y = std::abs(y);
        
        while (0 < q.size()) {
            LOC_MOVE currentSpotAndMove = q.front();
            q.pop();
            
            const int currentSpotX = currentSpotAndMove.first.first;
            const int currentSpotY = currentSpotAndMove.first.second;
            const int currentMove = currentSpotAndMove.second;
            
            if (currentSpotX == x && currentSpotY == y) return currentMove;
            
            for (auto const & move : moves) {
                const int xMove = move.first;
                const int yMove = move.second;
                const int nextSpotX = currentSpotX + xMove;
                const int nextSpotY = currentSpotY + yMove;
                
                if (nextSpotX < -2 || nextSpotY < -2) continue;
                if (1 < nextSpotX - x || 1 < nextSpotY - y) continue;
                
                const LOC nextSpot = {nextSpotX, nextSpotY};
                if (visited.find(nextSpot) != visited.end()) continue;
                
                LOC_MOVE nextSpotAndMove = { nextSpot, currentMove + 1};
                q.push(nextSpotAndMove);
                visited.insert(nextSpot);
            }
        }
        
        return -1;   
    }
};





// 71st percentile
class Solution {
public:
    typedef std::pair<int, int> LOC;
    typedef std::pair<LOC, int> LOC_MOVE; 
    
    std::vector<std::pair<int,int> > moves = { {1, 2}, {-1, 2}, {-1, -2}, {1, -2}, {2, 1}, {-2, 1}, {-2, -1}, {2, -1} };
    
    int minKnightMoves(int x, int y) {
        if (x == 0 && y == 0) return 0;
        
        std::queue<LOC_MOVE> q;
        std::unordered_set<LOC, pair_hash> visited;
        
        const LOC startSpot = {0, 0};
        const LOC_MOVE startSpotAndMove = { startSpot, 0 };
        q.push(startSpotAndMove);
        visited.insert(startSpot);
        
        x = std::abs(x);
        y = std::abs(y);
        
        while (0 < q.size()) {
            LOC_MOVE currentSpotAndMove = q.front();
            q.pop();
            
            const int currentSpotX = currentSpotAndMove.first.first;
            const int currentSpotY = currentSpotAndMove.first.second;
            const int currentMove = currentSpotAndMove.second;
            
            if (currentSpotX == x && currentSpotY == y) return currentMove;
            
            for (auto const & move : moves) {
                const int xMove = move.first;
                const int yMove = move.second;
                const int nextSpotX = currentSpotX + xMove;
                const int nextSpotY = currentSpotY + yMove;
                
                if (nextSpotX < -2 || nextSpotY < -2) continue;
                if (1 < nextSpotX - x || 1 < nextSpotY - y) continue;
                
                const LOC nextSpot = {nextSpotX, nextSpotY};
                if (visited.find(nextSpot) != visited.end()) continue;
                
                LOC_MOVE nextSpotAndMove = { nextSpot, currentMove + 1};
                q.push(nextSpotAndMove);
                visited.insert(nextSpot);
            }
        }
        return -1;        
    }
      
    struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*31+v.second;
    }
};
};



// Using a class instead of a struct
class Solution {
public:
    typedef std::pair<int, int> LOC;
    typedef std::pair<LOC, int> LOC_MOVE;
    
    std::vector<std::pair<int,int>> moves = { {1, 2}, {-1, 2}, {-1, -2}, {1, -2}, {2, 1}, {-2, 1}, {-2, -1}, {2, -1} };
    
    int minKnightMoves(int x, int y) {
        if (x == 0 && y == 0) return 0;
        
        std::queue<LOC_MOVE> q;
        std::unordered_set<LOC, pair_hash> visited;
        
        const LOC startSpot = {0, 0};
        const LOC_MOVE startSpotAndMove = { startSpot, 0 };
        q.push(startSpotAndMove);
        visited.insert(startSpot);
        
        x = std::abs(x);
        y = std::abs(y);
        
        while (0 < q.size()) {
            LOC_MOVE currentSpotAndMove = q.front();
            q.pop();
            
            const int currentSpotX = currentSpotAndMove.first.first;
            const int currentSpotY = currentSpotAndMove.first.second;
            const int currentMove = currentSpotAndMove.second;
            
            if (currentSpotX == x && currentSpotY == y) return currentMove;
            
            for (auto const & move : moves) {
                const int xMove = move.first;
                const int yMove = move.second;
                const int nextSpotX = currentSpotX + xMove;
                const int nextSpotY = currentSpotY + yMove;
                
                if (nextSpotX < -2 || nextSpotY < -2) continue;
                if (1 < nextSpotX - x || 1 < nextSpotY - y) continue;
                
                const LOC nextSpot = {nextSpotX, nextSpotY};
                if (visited.find(nextSpot) != visited.end()) continue;
                
                LOC_MOVE nextSpotAndMove = { nextSpot, currentMove + 1};
                q.push(nextSpotAndMove);
                visited.insert(nextSpot);
            }
        }
        return -1;        
    }
      
    class pair_hash {
        public:
            inline std::size_t operator()(const std::pair<int, int> & v) const {
                return v.first*31+v.second;
            }
};
};





// TODO
//     Bidirectional BFS
//     Some sort of dfs solution


/*
Intuition
    (1,1), (1,-1), (-1,-1) and (-1,1) will all have the same answer...
    so we can use those abs() to just reduce the problem to be a single quadrant
    and save some searching...

    we then do need
                if (nextSpotX < -2 || nextSpotY < -2) continue;
                if (1 < nextSpotX - x || 1 < nextSpotY - y) continue;
    to avoid timeouts...

    intuition for these - basically we're confining our search space from the box
    specified by 0,0 and our target:
        if (nextSpotX < -2 || nextSpotY < -2) continue;
            specifies confines on the bottom edge and the left edge
                for example, it might go from (0,0)
                to (-2, 1) and then back to (0, 2)
        
        if (1 < nextSpotX - x || 1 < nextSpotY - y) continue;
            covers the top edge and the right edge
            basically says to not go too far up or over so as to avoid passing up the target

            you could replace the 1's with 2's to make it more intuitive. Using 1's eke out a tiny
            bit more performance and do work.
        



Hash Function details:
    C++ has built in hash functions for primitive types and strings but not user defined types like
    or pairs


    Hash functions in c++ return size_t...it's the native integer type (and the fastest)
    remember...size_t is an unsigned int the can store the theoretically largest number possible
    if we used unsigned int, we might get undefined behavior
    The struct at the bottom states how to convert a pair into a size_t

    unordered_set is defined such that the second argument passed to it is a hasher class
        "A unary function object type that takes an object of the same type as the elements as 
        argument and returns a unique value of type size_t based on it. This can either be a class
         implementing a function call operator or a pointer to a function (see constructor for an example). 
         This defaults to hash<Key>, which returns a hash value with a probability of collision 
         approaching 1.0/std::numeric_limits<size_t>::max().
        The unordered_set object uses the hash values returned by this function to organize its 
        elements internally, speeding up the process of locating individual elements.
        Aliased as member type unordered_set::hasher."

    so unordered_set is constructed to take a class with function call operator specified...
    

Note the use of struct instead of a nested class. Either works. The only difference is the default
access level, so with a nested class, we would need public:

*/


/*
Great problem for
    BFS
    Custom hash functions / pair intricacies
    Typedef
    C++ hash functions
*/