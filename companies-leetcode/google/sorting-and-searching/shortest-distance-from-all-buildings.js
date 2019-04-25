/*
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
*/
// 34th percentile. 328ms
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    var m = grid.length;
    var n = grid[0].length;
    
    var hits = Array.from( {length:m}, () => 
                         Array.from( {length:n}, () => 0));
    var dists = Array.from( {length:m}, () => 
                         Array.from( {length:n}, () => 0));
    
    // Flatten the array and then sum
    let numBuildings = grid.reduce( (a, b) => a.concat(b) )
                            .filter( (a) => a===1)
                            .reduce( (a, b) => a + b);  
    
    var bfs = function(j, i, grid) {
        let q = [ [j, i, 0] ];
        let buildingsSeen = 1;
        let visited = Array.from({ length: m}, () => 
                                 Array.from({length: n}, ()=>false));
        visited[j][i] = true;
        
        while (q.length > 0) {
            let c = q.shift();
            let y = c[0],
                x = c[1],
                d = c[2];
            
            // Check neighbors
            let neighbors = [ [y+1, x], [y-1, x], [y, x+1], [y, x-1] ];
            for ( let nxt = 0; nxt < neighbors.length; nxt++ ) {
                    j = neighbors[nxt][0],
                    i = neighbors[nxt][1];

                // Add children: in-bounds, not visited already, not an obstacle
                if ( j >= 0 && j < m && i >= 0 && i < n && visited[j][i]===false && grid[j][i]!==2) {
                    visited[j][i] = true;
                    
                    // building
                    if (grid[j][i]===1) {
                        buildingsSeen++;
                    } else {
                        hits[j][i]++;
                        dists[j][i] += d+1;
                        q.push([j, i, d+1]);
                    }
                }
            }
        }
        return numBuildings === buildingsSeen;
    }
    
    
    // bfs for each city
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===1) {
                if (bfs(j, i, grid)===-1) {
                    return -1;
                }
            }
        }
    }
    
    // Identify solution 
    res = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===0 && hits[j][i]===numBuildings && dists[j][i] < res) {
                res = dists[j][i];
            }
        }
    }
    
    return res < Number.MAX_SAFE_INTEGER ? res : -1;
    
};




// 62nd percentile: 140ms
// Makes me sad, but filling the 2d arrays the simple way (not using from) is 
// more than twice as fast
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    var m = grid.length;
    var n = grid[0].length;
    
    var hits = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        hits.push(nxt);
    }
    
    var dists = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        dists.push(nxt);
    }
    
    
    // Flatten the array and then sum
    let numBuildings = grid.reduce( (a, b) => a.concat(b) )
                            .filter( (a) => a===1)
                            .reduce( (a, b) => a + b);  
    
    var bfs = function(j, i, grid) {
        let q = [ [j, i, 0] ];
        let buildingsSeen = 1;
        
        var visited = [];
        for (let j = 0; j < m; j++) {
            let nxt = [];
            for (let i = 0; i < n; i++) {
                nxt.push(false);
            }
            visited.push(nxt);
        }
        
        visited[j][i] = true;
        
        while (q.length > 0) {
            let c = q.shift();
            let y = c[0],
                x = c[1],
                d = c[2];
            
            // Check neighbors
            let neighbors = [ [y+1, x], [y-1, x], [y, x+1], [y, x-1] ];
            for ( let nxt = 0; nxt < neighbors.length; nxt++ ) {
                    j = neighbors[nxt][0],
                    i = neighbors[nxt][1];

                // Add children: in-bounds, not visited already, not an obstacle
                if ( j >= 0 && j < m && i >= 0 && i < n && visited[j][i]===false && grid[j][i]!==2) {
                    visited[j][i] = true;
                    
                    // building
                    if (grid[j][i]===1) {
                        buildingsSeen++;
                    } else {
                        hits[j][i]++;
                        dists[j][i] += d+1;
                        q.push([j, i, d+1]);
                    }
                }
            }
        }
        return numBuildings === buildingsSeen;
    }
    
    
    // bfs for each city
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===1) {
                if (bfs(j, i, grid)===-1) {
                    return -1;
                }
            }
        }
    }
    
    // Identify solution 
    res = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===0 && hits[j][i]===numBuildings && dists[j][i] < res) {
                res = dists[j][i];
            }
        }
    }
    
    return res < Number.MAX_SAFE_INTEGER ? res : -1;
    
};



// 36th percentile. 300ms
// dup grid helper method no go...
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    
    var dupGrid = function(grid, value) {
        const duplicate = JSON.parse(JSON.stringify(grid));

        duplicate.forEach( (row, rowIdx) => {
          row.forEach( (element, colIdx) => {
            duplicate[rowIdx][colIdx] = value;
          });
        });
        
        return duplicate;
    }
    
    
    var m = grid.length;
    var n = grid[0].length;    
    var hits = dupGrid(grid, 0);
    var dists = dupGrid(grid, 0);

    // Flatten the array and then sum
    let numBuildings = grid.reduce( (a, b) => a.concat(b) )
                            .filter( (a) => a===1)
                            .reduce( (a, b) => a + b);  
    
    var bfs = function(j, i, grid) {
        let q = [ [j, i, 0] ];
        let buildingsSeen = 1;
        
        var visited = dupGrid(grid, false);     
        visited[j][i] = true;
        
        while (q.length > 0) {
            let c = q.shift();
            let y = c[0],
                x = c[1],
                d = c[2];
            
            // Check neighbors
            let neighbors = [ [y+1, x], [y-1, x], [y, x+1], [y, x-1] ];
            for ( let nxt = 0; nxt < neighbors.length; nxt++ ) {
                    j = neighbors[nxt][0],
                    i = neighbors[nxt][1];

                // Add children: in-bounds, not visited already, not an obstacle
                if ( j >= 0 && j < m && i >= 0 && i < n && visited[j][i]===false && grid[j][i]!==2) {
                    visited[j][i] = true;
                    
                    // building
                    if (grid[j][i]===1) {
                        buildingsSeen++;
                    } else {
                        hits[j][i]++;
                        dists[j][i] += d+1;
                        q.push([j, i, d+1]);
                    }
                }
            }
        }
        return numBuildings === buildingsSeen;
    }
    
    
    // bfs for each city
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===1) {
                if (bfs(j, i, grid)===-1) {
                    return -1;
                }
            }
        }
    }
    
    // Identify solution 
    res = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===0 && hits[j][i]===numBuildings && dists[j][i] < res) {
                res = dists[j][i];
            }
        }
    }
    
    return res < Number.MAX_SAFE_INTEGER ? res : -1;
    
};




// 62nd percentile. 132ms.
// Object destructuring to try a different style. slight speedup too.
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    var m = grid.length;
    var n = grid[0].length;
    
    var hits = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        hits.push(nxt);
    }
    
    var dists = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        dists.push(nxt);
    }
    
    
    // Flatten the array and then sum
    let numBuildings = grid.reduce( (a, b) => a.concat(b) )
                            .filter( (a) => a===1)
                            .reduce( (a, b) => a + b);  
    
    
    
    
    var bfs = function(j, i, grid) {
        let q = [ {y: j, x:i, d: 0} ]
        let buildingsSeen = 1;
        
        var visited = [];
        for (let j = 0; j < m; j++) {
            let nxt = [];
            for (let i = 0; i < n; i++) {
                nxt.push(false);
            }
            visited.push(nxt);
        }
        
        visited[j][i] = true;
        
        while (q.length > 0) {
            let {y, x, d} = q.shift();
            
            // Check neighbors
            let neighbors = [ {j: y+1, i: x}, {j: y-1, i: x}, {j: y, i: x+1}, {j: y, i: x-1} ];
            for ( let nxt = 0; nxt < neighbors.length; nxt++ ) {
                let {j, i} = neighbors[nxt];    

                // Add children: in-bounds, not visited already, not an obstacle
                if ( j >= 0 && j < m && i >= 0 && i < n && visited[j][i]===false && grid[j][i]!==2) {
                    visited[j][i] = true;
                    
                    // building
                    if (grid[j][i]===1) {
                        buildingsSeen++;
                    } else {
                        hits[j][i]++;
                        dists[j][i] += d+1;
                        // q.push([j, i, d+1]);
                        q.push( {y: j, x: i, d: d+1} );
                    }
                }
            }
        }
        return numBuildings === buildingsSeen;
    }
    
    
    // bfs for each city
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===1) {
                if (bfs(j, i, grid)===-1) {
                    return -1;
                }
            }
        }
    }
    
    // Identify solution 
    res = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===0 && hits[j][i]===numBuildings && dists[j][i] < res) {
                res = dists[j][i];
            }
        }
    }
    
    return res < Number.MAX_SAFE_INTEGER ? res : -1;
    
};





// 100th percentile
/*
I was surprised my previous solutions weren't better...I have a really solid pruning
method here...I made a mistake before...I was checking if bfs returned -1 rather than
false. Switched this and boom, one of the best answers submitted. 
*/
/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestDistance = function(grid) {
    var m = grid.length;
    var n = grid[0].length;
    
    var hits = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        hits.push(nxt);
    }
    
    var dists = [];
    for (let j = 0; j < m; j++) {
        let nxt = [];
        for (let i = 0; i < n; i++) {
            nxt.push(0);
        }
        dists.push(nxt);
    }
    
    
    // Flatten the array and then sum
    let numBuildings = grid.reduce( (a, b) => a.concat(b) )
                            .filter( (a) => a===1)
                            .reduce( (a, b) => a + b);  
    
    
    
    
    var bfs = function(j, i, grid) {
        let q = [ {y: j, x:i, d: 0} ]
        let buildingsSeen = 1;
        
        var visited = [];
        for (let j = 0; j < m; j++) {
            let nxt = [];
            for (let i = 0; i < n; i++) {
                nxt.push(false);
            }
            visited.push(nxt);
        }
        
        visited[j][i] = true;
        
        while (q.length > 0) {
            let {y, x, d} = q.shift();
            
            // Check neighbors
            let neighbors = [ {j: y+1, i: x}, {j: y-1, i: x}, {j: y, i: x+1}, {j: y, i: x-1} ];
            for ( let nxt = 0; nxt < neighbors.length; nxt++ ) {
                let {j, i} = neighbors[nxt];    

                // Add children: in-bounds, not visited already, not an obstacle
                if ( j >= 0 && j < m && i >= 0 && i < n && visited[j][i]===false && grid[j][i]!==2) {
                    visited[j][i] = true;
                    
                    // building
                    if (grid[j][i]===1) {
                        buildingsSeen++;
                    } else {
                        hits[j][i]++;
                        dists[j][i] += d+1;
                        // q.push([j, i, d+1]);
                        q.push( {y: j, x: i, d: d+1} );
                    }
                }
            }
        }
        return numBuildings === buildingsSeen;
    }
    
    
    // bfs for each city
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===1) {
                if (bfs(j, i, grid)===false) {
                    return -1;
                }
            }
        }
    }
    
    // Identify solution 
    res = Number.MAX_SAFE_INTEGER;
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < n; i++) {
            if (grid[j][i]===0 && hits[j][i]===numBuildings && dists[j][i] < res) {
                res = dists[j][i];
            }
        }
    }
    
    return res < Number.MAX_SAFE_INTEGER ? res : -1;
    
};