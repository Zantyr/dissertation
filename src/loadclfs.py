from naivebayes import NaiveBayes,JobNaiveBayes,PersonalityNaiveBayes
from sys import argv
from svmclass import SVM,JobSVM,PersonalitySVM
#from kohonen import Kohonen
from kmeans import KMeans,JobKMeans,PersonalityKMeans
from scoring import HollandScoring,MBScoring
def loadclfs():
    #classifiers = {'kohonen':Kohonen,'bayes':NaiveBayes,'svm':SVM,'kmeans':KMeans}
    classifiers = [HollandScoring,MBScoring,NaiveBayes,SVM,KMeans,PersonalityNaiveBayes]

    def parse_test_data():
        jobflags = []
        vectors = []
        mbtiflags = []
        with open('static/tests','r') as f:
            for line in f:
                valid,vector = map(lambda x: eval(x),map(lambda x:x.strip(),line.split(';')))
                job = valid[0]
                mbti = valid[1]
                vectors.append(vector)
                jobflags.append(job)
                mbtiflags.append(mbti)
        return vectors,jobflags,mbtiflags

    try:
        with open(argv[1],'r'):
            pass #load classifier here
    except:
        clf = map(lambda x:x(),classifiers)
        clf = map(lambda x: x.fit(*parse_test_data()),clf) 
        for i in clf:
            print i.name 
    return clf
