:- dynamic(dead/0).

kill :- dead, !, fail.
kill :- asserta(dead).

resurrect :- dead, retract(dead), !.
resurrect :- !, fail.
