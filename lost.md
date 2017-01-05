\emph{Wstępna analiza danych}

\subsection{Redukcja wymiarowości}

Jednym z celów zastosowania EDA do tej aplikacji jest zredukowanie ilości pytań dla każdego z testów. Ograniczenie ilości pytań w modelu bierze się z dwóch przyczyn. Pierwszą z nich jest wygoda użytkownika - z założenia osoba biorąca udział w teście zawodowym nie jest skłonna wypełniać bardzo długich kwestionariuszy.

Druga cecha związana jest z dopasowaniem modeli do dużych zestawów danych. \emph{Curse of dimensionality} jest pojęciem związanym z uczeniem maszynowym i ogólnie pojętą analityką, opisujące postępujące rozrzedzenie danych w miarę wzrostu ich wymiarowości. (czy jest to prawda - źródła poddają w wątpliwość)

overfittign(nadmierne dopasowanie)

dla dziedziny X hipoteza h jest nadmiernie dopasowana, gdy istnieje hipoteza h' o większym błędzie próbki a mniejszym rzeczywistym

Nadmiernie dopasowana hipoteza oddaje przekłamania na danych. Ponadto, hipotezy zbyt dopasowane są porównywalne do interpolacji zaszumionych danych - po prostu zniekształcają obraz rzeczywistości. innymi słowy - bardziej trafne mogą być hipotezy niespójne na danych wejściowych








\subsection{Walidacja krzyżowa}

Błąd próbki:
$    e_P^c(h) = \frac{| \{ x \in P | h(x) != c(x) \} |}{|P|} $
    Liczba pomyłek:
$        r_P^c(h) = | \{ x \in P | h(x) != c(x) \} | $
Błąd rzeczywisty:
$    e_\Omega^c (h) = Pr_{x \in \Omega}(h(x) != c(x))$ gdzie Omega to rozkład prawdopodobieństa
    Możemy przypisać $\Omega$ jako jednorodnemu rozkładowi spośród próbki danych weryfikacyjnych
    

\section{Zagadnienie}

Wstęp: od ogólnej teorii uczenia. W teście mamy hipotezy cząstkowe oraz dane trenujące wywnioskowane ze skali

Każda hipoteza w przestrzeni hipotez klasyfikatora przypisuje dany wektor cech do jednej z sześciu kategorii (pojęcie wielokrotne)
