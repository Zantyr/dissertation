from naivebayes import NaiveBayes,JobNaiveBayes,PersonalityNaiveBayes
from sys import argv
from svmclass import SVM,JobSVM,PersonalitySVM
#from kohonen import Kohonen
from kmeans import KMeans,JobKMeans,PersonalityKMeans
def loadclfs():
    #classifiers = {'kohonen':Kohonen,'bayes':NaiveBayes,'svm':SVM,'kmeans':KMeans}
    classifiers = [NaiveBayes,SVM,KMeans]

    def parse_test_data():
        jobflags = []
        vectors = []
        with open('static/tests','r') as f:
            for line in f:
                job,vector = map(lambda x: eval(x),map(lambda x:x.strip(),line.split(';')))
                vectors.append(vector)
                jobflags.append(job)
        return vectors,jobflags

    try:
        with open(argv[1],'r'):
            pass #load classifier here
    except:
        clf = map(lambda x:x(),classifiers)
        clf = map(lambda x: x.fit(*parse_test_data()),clf) 
        for i in clf:
            print i.name 
    return clf
