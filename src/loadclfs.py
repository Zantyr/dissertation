from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
import numpy as np
import pandas

def kmeans(df,classes,colname='class'):
    return df.join(pandas.DataFrame(
        KMeans(n_clusters=classes).fit(df.as_matrix()).labels_,
        columns=[colname]))

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
    return model.predict(data)

def score(model,data):
    return model.score(data)