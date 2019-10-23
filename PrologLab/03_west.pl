criminal(X) :- american(X), weapon(Y), sells(X,Y,Z), hostile(Z), sells(X, Y, Z), hostile(Z).
sells(west, X, nono) :- missile(X), owns(nono,X).
weapon(X) :- missile(X).
hostile(Z) :- enemy(Z, america).

owns(nono, m1).
missile(m1).
american(west).
enemy(nono,america).


