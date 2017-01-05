Każda hipoteza w przestrzeni hipotez klasyfikatora przypisuje dany wektor cech do jednej z sześciu kategorii (pojęcie wielokrotne)

Czy klasyfikatory używane są spójne (błąd próbki = 0)?

Klasyfikacja to metoda indukcyjna, mianowicie stosujemy regułę P i W => K wstecz (pusty zbiór wiedzy początkowej i dane trenujące)



Klasyfikacja jest to uczenie pojęc







Wstęp: od ogólnej teorii uczenia. W teście mamy hipotezy cząstkowe oraz dane trenujące wywnioskowane ze skali

Klasyfikacja dzieli na grupy zwane kategoriami



Nauczalność pojęcia docelowego zachodzi wtedy gdy pojęcie docelowe c z przestrzeni pojęć C znajduje się w przestrzeni hipotez H. Oznacza to, że C musi być w H, gdy ma byc pewna nauczalność pojęcia

Duża przestrzeń hipotez utrudnia proces uczenia(overfittign)


Zapytanie - zgłoszenie przykładu do klasyfikacji. klasyfikacja = odpowiedź na zapytanie.
Odpowiadanie na zapytanie to stosowanie przyjętej przez ucznia hipotezy do przykłądów

Definicje pomijają niepoprawność danych. W przypadku danych anonimowych należy założyć, że część z nich będzie nietrafna

Błąd próbki:
e_P^c(h) = \frac{| \{ x \in P | h(x) != c(x) \} |}{|P|}
Liczba pomyłek:
r_P^c(h) = | \{ x \in P | h(x) != c(x) \} |}
Błąd rzeczywisty:
e_\Omega^c (h) = Pr_{x \in \Omega}(h(x) != c(x)) gdzie Omega to rozkład prawdopodobieństa
Możemy przypisać \Omega jako jednorodnemu rozkładowi spośród próbki danych weryfikacyjnych





Klasteryzacja to zadanie tworzenia pojęć bez uprzedniej wiedzy. Możliwe jest rozbicie problemu na dwa zadania: podział na grupy i nauki pojęć. Zazwyczaj realizuje to jedna metoda (kmeans na przykład), jednak można te dwa zadania rozdzielić


=====================
estymacja przedziałowa
PAC-nauczalność
minimalny rozmiar danych dla zbioru PAC-nauczalnego dla (\delta,\epsilon)
\frac{1}{\epsilon}(ln|H|+ln\frac{1}{\delta}) - co najwyżej wielomianowa złożoność algorytmu, by był efektywny
