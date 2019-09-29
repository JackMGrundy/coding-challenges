"""
Given a robot cleaner in a room modeled as a grid.                              

Each cell in the grid can be empty or blocked.                                  

The  robot  cleaner with 4 given APIs can move forward, turn left or turn right.
Each turn it made is 90 degrees.                                                

When  it  tries  to  move  into  a  blocked  cell, its bumper sensor detects the
obstacle and it stays on the current cell.                                      

Design  an  algorithm to clean the entire room using only the 4 given APIs shown
below.                                                                          

interface Robot {                                                               

  // returns true if next cell is open and robot moves into the cell.           

  // returns false if next cell is obstacle and robot stays on the current cell.

  boolean move();                                                               

  // Robot will stay on the same cell after calling turnLeft/turnRight.         

  // Each turn will be 90 degrees.                                              

  void turnLeft();                                                              

  void turnRight();                                                             

  // Clean the current cell.                                                    

  void clean();                                                                 

}                                                                               

Example:                                                                        

Input:                                                                          

room = [                                                                        

  [1,1,1,1,1,0,1,1],                                                            

  [1,1,1,1,1,0,1,1],                                                            

  [1,0,1,1,1,1,1,1],                                                            

  [0,0,0,1,0,0,0,0],                                                            

  [1,1,1,1,1,1,1,1]                                                             

],                                                                              

row = 1,                                                                        

col = 3                                                                         

Explanation:                                                                    

All grids in the room are marked by either 0 or 1.                              

0 means the cell is blocked, while 1 means the cell is accessible.              

The robot initially starts at the position of row=1, col=3.                     

From the top left corner, its position is one row below and three columns right.

Notes:                                                                          

The  input  is  only  given  to  initialize  the  room  and the robot's position
internally.  You must solve this problem "blindfolded". In other words, you must
control  the  robot  using  only  the mentioned 4 APIs, without knowing the room
layout and the initial robot's position.                                        

The robot's initial position will always be in an accessible cell.              

The initial direction of the robot will be facing up.                           

All  accessible  cells are connected, which means the all cells marked as 1 will
be accessible by the robot.                                                     

Assume all four edges of the grid are all surrounded by wall.                   

"""





"""
Notes:

Kind  of  reminds  me  of  the problems from Sutton and Barto. If we had all the
coordinates  of the graph and could simply state the square we wanted to move to
(up,  left,  right,  down),  this would be textbook backtracking/dfs. The tricky
parts  are  a) figuring out how to label the "seen" squares in this "dark" maze.
b)  translating  the  turnleft  and turnright commands to "up", "left", "right",
"down" c) unlike dfs with a stack, we can't just pop off a deadend to backtrack.
Here  we  actually  have  to  make the robot go back to the last point we had an
alternate path.                                                                 

This complications make this problem interesting. Here's the strategy:          

recursive/dfs                                                                   

each  recursive  call  takes  the  robot, the current "location" x,y the current
"direction" dx,dy, and a set of visited.                                        

At  the  start of the call, clean whatever square we're at and record the square
as visited.                                                                     

Then  we'll  have  a for loop with the real meat and potatoes. This loop will be
for 0 to 4...4 iterations for each of the 4 cardinal directions.                

We're  going  to  add up the x+dx and y+dy to get the target square. We check if
we've been there before and we try to move there.                               

If succesfully move to the square:                                              

spin up another dfs call                                                        

Then  we  have  a  clever  bit...If  the  spun  up dfs call sucessfully moves us
forward,  we'll need to retreat when we're backtracking. We can do that with two
left  turns,  a move, and then two left turns. This basically says "turn around"
move  to  the  last  square  "then  turn  back  around  so we're facing the same
direction we were when we were last at that square"                             

Regardless of whether we succesfully move to the square:                        

Next  we're  going to rotate left. If we failed to move to the square, then this
essentially is saying to turn left and try that way in the next iteration of the
loop.  If  we  did suceed in moving to the square, the all of the spun dfs calls
will  have  since  terminated and we've backtracked...so whether or not the call
succeeds, we're in the same square facing the same direction.                   

The  final bit is that we need to update dx and dy for the next iteration of the
for  loop.  Since  we're using left turns, we'll want to update the dx and dy so
that they change in a counteclockwise pattern. A nifty trick to do that:        

dx, dy = -dy, dx                                                                

dx = 0, dy = 1     up                                                           

dx = -1, dy = 0    left                                                         

dx = 0, dy = -1    down                                                         

dx = 1, dy = 0     right                                                        

dx = 0, dy = 1     up                                                           

Without the negative sign, this would would just keep swapping between          

dx = 0, dy = 1  and dx = 1, dy = 0                                              

The negative sign makes it cycle through all 4 orthogonal directions...like with
complex numbers...                                                              

And  that  does  it.  Note,  this  stratgy  comes from the "always turn one way"
strategy of solving a maze with defined edges.                                  


"""