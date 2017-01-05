Klasyfikacja, Klasteryzacja. Regresja - trzy kluczowe zadania analizy danych (modeli predykcyjnych)

Data Mining to zetknięcie statystyki i machine learningu




CELEM DA JEST WNIOSKOWANIE
Indukcyjne: training information -> knowledge (specific to general)
Dedukcyjne: knowledge + query -> answer

Domain
Instances
Attributes
  nominal, ordinal, interval, ratio
Target Attributes
Input Attribute
Training set
model
Performance
Generalisation
  celem indukcyjnego ML jest uogólnianie
Overfitting
  overfitting to efekt złej eneralizacji
Algorytmy
  weight-sensitive algorithms
  inductive bias




Warto przyjrzeć się grupowaniu hierarchicznemu
Jest to drzewo płaskich modeli klastrujących

Similarity/dissimilarity driven clustering
probabilistic clustering
descriptive vs prescriptive





Problemy z danymi:
  niekompletne dane
  zaszumione dane



Podstawowe miary df.describe()



Outlier detection:
  below/above quartiles by a coeff*inter-quartile range

mode(most occuring data point), weighted-mode,




relationship detection:
  significance tests
    null and alternative hypotheses
  p-value
  false positives/negatives

  Correlations may occur only in continuous data

Relationships in discrete values:
  chi-squared test (korelacja między dwiema zmiennymi)

p-value dredging

ANOVA?









Visualisation:
* Boxplot
* Histogram
* Barplot






Bayes is not robust to zero/small probabilities, not occuring in the sample



Naivety of the classifier is based on the assumption of independence
Sieci Bayesowskie biorą pod uwagę złamanie tego założenia.


Bias and variance in tests
