/** For example  [3, 9, 6]  where minimum is 4 and maximum is 10 **/

knapsack([], K, Min, Max) :- sum(K, X), X >= Min, X =< Max.
knapsack([F|R], K, Min, Max) :- knapsack(R, [F|K], Min, Max).
knapsack([_|R], K, Min, Max) :- knapsack(R, K, Min, Max).

sum([], 0) :- !.
sum([H|T], X) :- sum(T, Y), X == H + Y, !.

/**
test([], K) :- !.
test([H|T], [H|K]) :- test(T, [H|K]).
test([_|T], K) :- test(T, K).
**/

/**
merge_sort([], []).
merge_sort(L1, X) :- halve2(L1, H1, H2), merge_sort(H1, L1), merge_sort(H2, L2), merge(L1, L2, X).

merge([], [], []).
merge([A|R1], [B|R2], [A|R3]) :- A < B, merge(R1, [B|R2], R3).
merge([A|R1], [B|R2], [B|R3]) :- B < A, merge([A|R1], R2, R3).

halve2(L,A,B):-hv2(L,L,A,B).
   
hv2([],R,[],R).   % for lists of even length
hv2([_],R,[],R).  % for lists of odd length
hv2([_,_|T],[X|L],[X|L1],R):-hv2(T,L,L1,R).
**/

nodups([]) :- !.
nodups([F|R]) :- notmember(F, R), nodups(R).

notmember(_, []).
notmember(E, [E|_]) :- fail, !.
notmember(E, [F|R]) :- F \= E, notmember(E, R).

notmember2(E, L) :- \+ member(E, L).