from sklearn.naive_bayes import BernoulliNB
from selectors import PersonalitySelector,JobSelector
import numpy as np
NaiveBayes = BernoulliNB
NaiveBayes.fit = lambda self,inp,desired: super(NaiveBayes,self).fit(\
                        np.array(inp),np.array(desired))
NaiveBayes.name = "Naiwny klasyfikator bayesowski"

class JobNaiveBayes(JobSelector):
    def __init__(self):
        super(JobNaiveBayes,self).__init__()
        self.model = NaiveBayes()

class PersonalityNaiveBayes(PersonalitySelector):
    def __init__(self):
        super(PersonalityNaiveBayes,self).__init__()
        self.model = NaiveBayes()
