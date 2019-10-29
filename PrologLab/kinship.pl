parent(a,b).              
parent(a,c).
parent(b,d).
parent(b,e).
parent(c,f).

person(X) :- parent(X, _).
person(X) :- parent(_,X).

% sibling(X, Y) true is X and Y are different, but have the same parent
sibling(X, Y) :- person(X), person(Y), X \= Y, parent(Z,X), parent(Z,Y).