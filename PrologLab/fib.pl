/*
  The Fibonacci sequence is defined as fib(x) = fib(x-2) + fib(x-1) where x > 0, and fib(0) = 0, and fib(1) = fib(2) = 1
  Write the predicate fib(N, M) which should fail for N < 0
  */.
  
fib(N,_) :- fail, !.

fib(0,0) :- !.
fib(1, 1) :- !.
fib(2, 1) :- !.

fib(N, M) :- NN is N - 1, NNN is N - 2, fib(NN, X1), fib(NNN, X2), M is X1 + X2.
