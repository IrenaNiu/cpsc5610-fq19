/**
  DELETE THIS COMMENT PRIOR TO HANDING IN
  
  First test the game by consulting this file, then try the following commands
      look.   -- Tells you about your surroundings
	  move(north). move(south). move(east). move(west).  -- Like it sounds
  
  Now extend the game in the three following ways:
  
  	1.  Display pit and wumpus when in the square
    2.  Pickup gold action
	3.  Win
	
1.  If you walk into a square that contains a Wumpus or a Pit, you die and you can no 
    longer move, but the look command does not tell you what is the square (Wumpus or Pit).  
	Extend the look command to do that.
2.  Agent can see the gold, but cannot pick it up.  Implement a command pickup, which causes
    the agent to be holding the gold, and the cell is no longer holding the gold.  The look 
	command should indicate that the agent is holding the gold.
3.  Winning the game.  If the agent is at [1,1] and is holding the gold, the agent wins. 
	The look command should display that the agent has won, and having won, the agent can no 
	longer execute the move command.
	
**/

/**

north moves up    -- move to smaller row
south moves down  -- move to larger row
west moves left   -- move to smaller column
east moves right  -- move to larger column

Coordinate system:  [1,1] is at upper left, order is (row, col)
[1,1]   [1,2]  [1,3]
|-----|------|-------|
|
|  A      
|-----|------|-------|
|         P
|
|-----|------|-------|
|               
|  W       G
|------|------|------|

Functionality:
-- look
  -- shows location
  -- shows pit, wumpus, gold
  -- shows holding gold (NOT IMPLEMENTED)
  -- shows dead
  -- shows won (NOT IMPLEMENTED)
-- move(dir)
-- pickup (NOT IMPLEMENTED)


**/

/** Initial state **/
:- dynamic(contains/3).
:- dynamic(dead/0).

size(3).
contains(1,1, agent).
contains(2,2, pit).
contains(3,1, wumpus).
contains(3,2, gold).

reset :- retractall(contains(_,_,_)),
			asserta(dead),    % Need the assert because retract fails if the fact is not asserted
			retract(dead),
			asserta(contains(1,1, agent)),
			asserta(contains(2,2, pit)),
			asserta(contains(3,1, wumpus)),
			asserta(contains(3,2, gold)).

/** Look **/
look :- look_contains, look_dead, look_wumpus, look_pit, look_gold.

look_contains :- contains(R, C, agent), write('You are at '), write(R), write(' '), write(C), write('\n'), !.

look_dead :- dead, write('You are dead.'),!.
look_dead :- !.

look_wumpus :- contains(R,C, agent), RP is R - 1, contains(RP,C, wumpus), write('Wumpus adjacent\n'), !.
look_wumpus :- contains(R,C, agent), RP is R + 1, contains(RP,C, wumpus), write('Wumpus adjacent\n'), !.
look_wumpus :- contains(R,C, agent), CP is C - 1, contains(R,CP, wumpus), write('Wumpus adjacent\n'), !.
look_wumpus :- contains(R,C, agent), CP is C + 1, contains(R,CP, wumpus), write('Wumpus adjacent\n'), !.
look_wumpus :- !.

look_pit :- contains(R,C, agent), RP is R - 1, contains(RP,C, pit), write('Pit adjacent\n'), !.
look_pit :- contains(R,C, agent), RP is R + 1, contains(RP,C, pit), write('Pit adjacent\n'), !.
look_pit :- contains(R,C, agent), CP is C - 1, contains(R,CP, pit), write('Pit adjacent\n'), !.
look_pit :- contains(R,C, agent), CP is C + 1, contains(R,CP, pit), write('Pit adjacent\n'), !.
look_pit :- !.

look_gold :- contains(R,C,agent), contains(R,C,gold), write('Gold here.'), !.
look_gold :- !.

dead :- contains(R,C,agent), contains(R,C,wumpus).
dead :- contains(R,C,agent), contains(R,C,pit).

move(D) :- \+ dead, 
			D == south, 
			contains(R,C,agent), 
			size(S),
			R < S,
			retract(contains(R,C,agent)), 
			NewR is R + 1, 
			asserta(contains(NewR, C, agent)),
			!.
move(D) :- \+ dead, 
			D == north, 
			contains(R,C,agent), 
			1 < R,
			retract(contains(R,C,agent)), 
			NewR is R - 1, 
			asserta(contains(NewR, C, agent)),
			!.
			
move(D) :- \+ dead, 
			D == east, 
			contains(R,C,agent), 
			size(S),
			C < S,
			retract(contains(R,C,agent)), 
			NewC is C + 1, 
			asserta(contains(R, NewC, agent)),
			!.
			
move(D) :- \+ dead, 
			D == west, 
			contains(R,C,agent), 
			1 < C,
			retract(contains(R,C,agent)), 
			NewC is C - 1, 
			asserta(contains(R, NewC, agent)),
			!.

