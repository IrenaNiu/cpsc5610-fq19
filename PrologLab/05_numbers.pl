factorial(1,1) :- !.
factorial(X, R) :- XX is X-1, factorial(XX, T), R is  X * T.

