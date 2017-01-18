\subsection{Redukcja wymiarowości}

Redukcja wymiarowości jest zagadnieniem pozwalającym na lepsze wykorzystanie modelu. Skuteczność modeli SI zależy od założenia niezależności zmiennych jak i od ilości wymiarów.

W zależności od tego, czy zachowana jest ilość zmiennych branych pod uwagę, wyróżnia się selekcję cech i ich redukcję (polskie tłumaczenia?) Selekcja polega na wybraniu najbardziej kluczowych zmiennych z danego zestawu danych. W niniejszej pracy selekcja pozwala zredukować liczbę pytań, co wpłynie na komfort ankietowanego. Drugą metodą jest redukcja, która polega na wiązaniu zmiennych w taki sposób, aby otrzymać nowy zbiór zmiennych o niższej liczności, które możliwie dokładnie odzwierciedlają zestaw danych.

Feature selection, Metody używane:

Variance Threshold
Univariate feature selection

Progowanie wariancji polega na selekcji tych cech, których wariancja jest powyżej ustalonego progu.
Jednowymiarowa selekcja cech polega 

\bibitem{feature-selection-sources} http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.559.7830&rep=rep1&type=pdf

Feature reduction:

Redukcja wymiarowości...

Celem redukcji wymiarowości jest uproszczenie danych przekazywanych do klasyfikatora w celu poprawy jego trafności.

Analiza składowych głównych (PCA - primary component analysis) opiera się na przekształceniu n-wymiarowej przestrzeni zmiennych zależnych na zbiór n wektorów wzajemnie ortogonalnych uszeregowanych względem malejącej wariancji danych. Spośród tych wektorów następnie wybiera się pożądaną ilość cech, które posłużą do dalszej klasyfikacji.

Wzór wektorowy tutaj

\bibitem{scikit-learn} http://scikit-learn.org/stable/modules/feature_selection.html
\bibitem{stanisz} Andrzej Stanisz, "Przystępny kurs statystyki z zastosowaniem STATISTICA PL na przykładach z medycyny. Tom 3. Analizy wielowymiarowe", Kraków 2007