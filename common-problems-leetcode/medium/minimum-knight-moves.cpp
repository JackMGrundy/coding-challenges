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




// 44th percentile
class Solution {
public:
    typedef std::pair<int, int> LOC;
    typedef std::pair<LOC, int> LOC_MOVE;
    
    std::vector<std::pair<int,int>> moves = { {1, 2}, {-1, 2}, {-1, -2}, {1, -2}, {2, 1}, {-2, 1}, {-2, -1}, {2, -1} };
    
    int minKnightMoves(int x, int y) {
        if (x == 0 && y == 0) return 0;
        
        std::queue<LOC_MOVE> q;
        set<LOC> visited;
        
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
                if (nextSpotX - x > 1 || nextSpotY - y > 1) continue;
                
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
    
    std::vector<std::pair<int,int>> moves = { {1, 2}, {-1, 2}, {-1, -2}, {1, -2}, {2, 1}, {-2, 1}, {-2, -1}, {2, -1} };
    
    int minKnightMoves(int x, int y) {
        if (x == 0 && y == 0) return 0;
        
        std::queue<LOC_MOVE> q;
        unordered_set<LOC, pair_hash> visited;
        
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
                if (nextSpotX - x > 1 || nextSpotY - y > 1) continue;
                
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



// TODO
//     Bidirectional BFS
//     Some sort of dfs solution



/*
Great problem for
    BFS
    Custom hash functions / pair intricacies
    Typedef
*/