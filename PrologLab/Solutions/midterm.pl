/*
jonas owns a gold bracelet
Things made of gold and silver are shiny, as are diamonds
Bracelets are jewelry.
anybody who owns shiny jewelry makes all of their insecure friends jealous
jonas's only two friends are abel and baker, and baker is insecure
*/

owns(jonas, gb).

gold(gb).
bracelet(gb).

shiny(X) :- gold(X).
shiny(diamonds).

jewelry(X) :- bracelet(X).

jealous(X, Y) :- owns(Y, O), jewelry(O), shiny(O), friend(X, Y), insecure(X).

friend(abel, jonas).
friend(baker, jonas).
friend(X, Y) :- X \= Y, friend(Y, X).

insecure(baker).
