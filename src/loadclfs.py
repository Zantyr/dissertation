#-*- coding:utf-8; -*-
from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import numpy as np
import pandas

def kmeans(df,classes,colname='class'):
    """
    Funkcja używana przy konstrukcji raportów
    Klastruje dane na *classes* elementów i dodaje je wynik do zestawu danych
        pod nazwą *colname*
    """
    return df.join(pandas.DataFrame(
        KMeans(n_clusters=classes).fit(df.as_matrix()).labels_,
        columns=[colname]))


#Nadpisanie funkcji do wbudowanych klasyfikatorów Pythona, aby akceptowały
#    argumenty podawane w skryptach konfiguracyjnych
NaiveBayes = MultinomialNB
NaiveBayes.fit = lambda self,col,df: (super(NaiveBayes,self).fit(\
                        np.array(df.select(lambda x:unicode(x)!=col,1)),
                        np.array(df.select(lambda x:unicode(x)==col,1))),
                            setattr(self,'column',col))
NaiveBayes.score = lambda self,df: super(NaiveBayes,self).score(\
                        np.array(df.select(lambda x:unicode(x)!=self.column,1)),
                        np.array(df.select(lambda x:unicode(x)==self.column,1)))

SVM = SVC
SVM.fit = lambda self,col,df: (super(SVM,self).fit(\
                        np.array(df.select(lambda x:unicode(x)!=col,1)),
                        np.array(df.select(lambda x:unicode(x)==col,1))),
                            setattr(self,'column',col))
SVM.score = lambda self,df: super(SVM,self).score(\
                        np.array(df.select(lambda x:unicode(x)!=self.column,1)),
                        np.array(df.select(lambda x:unicode(x)==self.column,1)))

def fit(model,col,df):
    """
    Funkcja odpowiedzialna za tworzenie nowych modeli i trenowanie ich
    """
    if model=="naiveBayes":
        nb = NaiveBayes()
        nb.fit(col,df)
        return nb
    if model=="SVM":
        sv = SVM()
        sv.fit(col,df)
        return sv
    if model=="SVM:c=3":
        sv = SVM(C=3)
        sv.fit(col,df)
        return sv

def predict(model,data):
    """
    Wrapper do raportowania
    """
    return model.predict(data)

def score(model,data):
    """
    Wrapper do raportowania
    """
    return model.score(data)
