from sklearn.naive_bayes import BernoulliNB
import numpy as np
NaiveBayes = BernoulliNB
NaiveBayes.fit = lambda self,inp,desired: super(NaiveBayes,self).fit(\
                        np.array(inp),np.array(desired))
NaiveBayes.name = "Naiwny klasyfikator bayesowski"
