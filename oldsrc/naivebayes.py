from sklearn.naive_bayes import BernoulliNB
from selectors import PersonalitySelector,JobSelector
import numpy as np
NaiveBayes = BernoulliNB
NaiveBayes.fit = lambda self,inp,desired,_: super(NaiveBayes,self).fit(\
                        np.array(inp),np.array(desired))
NaiveBayes.name = "Naiwny klasyfikator bayesowski"

def numtombti(num):
    return tuple([1 if x else -1 for x in (num%2, int(num%4/2),int(num%8/4),int(num/8))])

class JobNaiveBayes(JobSelector):
    def __init__(self):
        super(JobNaiveBayes,self).__init__()
        self.model = NaiveBayes()

class PersonalityNaiveBayes(PersonalitySelector):
    def __init__(self):
        super(PersonalityNaiveBayes,self).__init__()
        self.model = NaiveBayes()
        self.model.fit = lambda inp,_,desired: super(NaiveBayes,self.model).fit(\
                        np.array(inp),np.array(desired))
        self.model.predict = lambda data: numtombti(super(NaiveBayes,self.model).predict(data))
