/*
   xmember(Element, Set)
   xintersection(Set1, Set2, SetI)
   xunion(Set1, Set2, SetU)
   
*/

xmember(_,[]) :- !,fail.
xmember(E, [E|_]) :- !.
xmember(E, [_|R]) :- xmember(E,R).

xintersection([], _, []) :- !.
xintersection([F|R], S, [F|A]) :- xmember(F,S), xintersection(R, S, A), !.
xintersection([_|R], S, T) :- xintersection(R, S, T).

/*  Kind of a cheaty way to do union.... just append the lists together and remove dups */
xappend([], X, X).
xappend([X|Y], Z, [X|W]) :- append(Y, Z, W).

xdedupe([], []).
xdedupe([X], [X]).
xdedupe([F|X], [F|Y]) :- \+ xmember(F,X), !, xdedupe(X, Y).
xdedupe([_|X], Y) :- xdedupe(X, Y).

xunion(A, B, Z) :- xappend(A, B, D), xdedupe(D, Z).