/*  In order to allow Prolog to "iterate over" individuals, you have to identify a set of 
    individuals to "iterate" over.  Here we define the set of "persons", and then define sibling,
	cousin, etc. in terms of persons */

/*  This says "a is the parent of b" so be aware of the order of arguments */
parent(a,b).              
parent(a,c).
parent(b,d).
parent(b,e).
parent(c,f).

/*  Enumerate the list of all persons on the basis of teh parent relationships above */
person(X) :- parent(X, _).
person(X) :- parent(_, X).

% Just a change of terminology.
% Might be helpful because in the examples below it's easier to talk about "child" than "parent"

child(X, Y) :- person(X), person(Y), parent(Y,X).

% sibling(X, Y) true is X and Y are different, but have the same parent
sibling(X, Y) :- person(X), person(Y), X \= Y, parent(Z,X), parent(Z,Y).

% cousin(X, Y), true if X and Y are different, and X's parent and Y's parent are siblings
cousin(X,Y) :- person(X), person(Y), X \= Y, parent(A, X), parent(B,Y), sibling(A,B).

% grandchild(X, Y) true if the parent of X's parent is Y
grandchild(X, Z) :- person(X), person(Z), child(X,Y), child(Y,Z).

% X is a descendent of Y
% descendent(X, Y) true if there is a chain of parent relationships leading from X to Y
descendent(X, Y) :- person(X), person(Y), child(X, Y).
descendent(X, Z) :- person(X), person(Z), child(X,Y), descendent(Y,Z).

