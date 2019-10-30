/*  This is the simpler version of the problem.  You can say sibling(b,c) for example, but
     you can't say sibling(X,Y) because there is not a "universe" of individuals to quantify over */

/*  This says "a is the parent of b" so be aware of the order of arguments */
parent(a,b).              
parent(a,c).
parent(b,d).
parent(b,e).
parent(c,f).

% Just a change of terminology.
% Might be helpful because in the examples below it's easier to talk about "child" than "parent"

child(X, Y) :- parent(Y,X), !.

% sibling(X, Y) true is X and Y are different, but have the same parent
sibling(X, Y) :- X \= Y, parent(Z,X), parent(Z,Y).

% cousin(X, Y), true if X and Y are different, and X's parent and Y's parent are siblings
cousin(X,Y) :- X \= Y, parent(A, X), parent(B,Y), sibling(A,B).

% grandchild(X, Y) true if the parent of X's parent is Y
grandchild(X, Z) :- child(X,Y), child(Y,X).

% X is a descendent of Y
% descendent(X, Y) true if there is a chain of parent relationships leading from X to Y
descendent(X, Y) :- child(X, Y).
descendent(X, Z) :- child(X,Y), descendent(Y,Z).

/*  Tests
  child(f,c).
  sibling(b,c).
  grandchild(e,a).
  descendent(d,e).
  descendent(b,a).
  
  (You should also try other relationships that should fail.)
*/