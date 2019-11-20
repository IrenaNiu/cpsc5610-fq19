%nodups([]).
%nodups([F|R]) :- \+ member(F, R), nodups(R).

xfirst([F|_], F).

xsecond([_|R], S) :- xfirst(R, S).

xnth([], _, _) :- fail, !.
xnth([F|_], 0, F).
xnth([_|R], N, Q) :- NN is N - 1, xnth(R, NN, Q).

/**                         **/

nodups([]).
nodups([F|R]) :- \+ member(F, R), nodups(R).

merge([], [], []) :- !.
merge(L, [], L) :- !.
merge([], L, L) :- !.
merge([A|B], [C|D], [A|R]) :- A =< C, merge(B, [C|D], R).
merge([A|B], [C|D], [C|R]) :- C < A, merge([A|B], D, R).