from sklearn.cluster import KMeans
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas

def kmeans(df,classes,colname='class'):
    return df.join(pandas.DataFrame(
        KMeans(n_clusters=classes).fit(df.as_matrix()).labels_,
        columns=[colname]))

NaiveBayes = MultinomialNB
NaiveBayes.fit = lambda self,col,df: super(NaiveBayes,self).fit(\
                        np.array(df.select(lambda x:unicode(x)!=col,1)),
                        np.array(df.select(lambda x:unicode(x)==col,1)))

def fit(model,col,df):
    if model=="naiveBayes":
        nb = NaiveBayes()
        nb.fit(col,df)
        return nb

def predict(model,data):
    return model.predict(data)