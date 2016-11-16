import sys
import os
from subprocess import Popen,PIPE
import random
from selectors import PersonalitySelector,JobSelector

class SVM(object):
    def __init__(self,suffix=''):
        self.suffix=suffix
        self.name = "Klasyfikator maksymalnoodleglosciowy"
    def fit(self,input,desired):
        identifier = self._random_id()
        with open("static/svm{0}.tmp".format(self.suffix),"w") as f:
            f.write('\n'.join(
                map(
                    lambda (i,j):
                        str(j) +
                             ''.join(map(lambda (x,y):" {0}:{1}".format(str(x),str(y)),enumerate(i))),
                           zip(input,desired))))
        cmd = 'libsvm/svm-train "static/svm{0}.tmp" "static/svm{0}.model"'.format(self.suffix)
        Popen(cmd, shell = True, stdout = PIPE).communicate()  
        os.remove("static/svm{0}.tmp".format(self.suffix))
        return self   
    def predict(self,data):
        identifier = self._random_id()
        with open("static/svm.in.{}".format(identifier),"w") as f:
            f.write('\n'.join(
                map(
                    lambda i:
                        "0 " +
                             ''.join(map(lambda (x,y):" {0}:{1}".format(str(x),str(y)),enumerate(i))),
                           data)))
        cmd = 'libsvm/svm-predict "static/svm.in.{0}" "static/svm{1}.model" "static/svm.out.{0}"'.format(identifier,self.suffix)
        Popen(cmd, shell = True, stdout = PIPE).communicate() 
        with open("static/svm.out.{0}".format(identifier),"r") as f:
            classification = int(f.read().strip())
        os.remove("static/svm.in.{0}".format(identifier))
        os.remove("static/svm.out.{0}".format(identifier))
        return classification
    def _random_id(self):
        return ''.join([str(random.randint(0,9)) for x in range(10)])

class JobSVM(JobSelector):
    def __init__(self):
        super(JobSVMself).__init__()
        self.model = SVM(suffix='job')

class PersonalitySVM(PersonalitySelector):
    def __init__(self):
        super(PersonalitySVM,self).__init__()
        self.model = SVM(suffix='pers')
