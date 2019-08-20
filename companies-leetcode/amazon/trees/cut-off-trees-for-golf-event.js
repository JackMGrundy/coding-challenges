/*
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Hint: size of the given matrix will not exceed 50x50.
*/
// 3080. Leetcode is having issues so can't tell performance...looks like 50th percentile roughly. 
/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
    let treesToCut = forest.concat.apply([], forest);
    treesToCut = [...new Set(treesToCut)];
    treesToCut = treesToCut.filter( tree => tree > 1 )
    treesToCut.sort( (a,b) => {
        return b-a;
    });
    
    let bfs = function(forest, targetTree, startY, startX) {
        let queue = [ [startY, startX, 0] ];
        let visitedSquares = new Set();
        
        while (queue.length > 0) {
            let current = queue.shift();
            const y = current[0];
            const x = current[1];
            const stepsTaken = current[2];
            
            if (visitedSquares.has("" + y + "," + x)) {
                continue;
            } else if (forest[y][x] === targetTree) {
                return [y, x, stepsTaken];
            } else {
                visitedSquares.add("" + y + "," + x);
                if (y+1 < forest.length && forest[y+1][x] !== 0) {
                    queue.push( [y+1, x, stepsTaken+1] );
                }
                if (y-1 >= 0 && forest[y-1][x] !== 0) {
                    queue.push( [y-1, x, stepsTaken+1] );
                }
                if (x+1 < forest[0].length && forest[y][x+1] !== 0) {
                    queue.push( [y, x+1, stepsTaken+1] );
                }
                if (x-1 >= 0 && forest[y][x-1] !== 0) {
                    queue.push( [y, x-1, stepsTaken+1] );
                }
            }
        }
        return [-1, -1, -1];
    }
    

    let stepsTaken = 0;
    let y = 0;
    let x = 0;
    while (treesToCut.length > 0) {
        const targetTree = treesToCut.pop();
        const res = bfs(forest, targetTree, y, x);
        const targetY = res[0];
        const targetX = res[1];
        const stepsToTarget = res[2];
        if (stepsToTarget === -1) {
            return -1;
        }
        y = targetY;
        x = targetX;
        stepsTaken += stepsToTarget;
    }
    
    return stepsTaken;
};