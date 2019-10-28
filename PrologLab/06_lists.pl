nodups([]).
nodups([F|R]) :- \+ member(F, R), nodups(R).

