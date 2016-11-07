import sys
sys.path.insert(0,"/media/arioch/adbf5f51-d439-433b-8e45-7c52b1f6b8e7/home/zantyr/dissertation/src/env/lib/python2.7/site-packages")
from pybrain.structure.modules.svmunit import SVMUnit
from pybrain.supervised.trainers.svmtrainer import SVMTrainer

class SVM(object):
    def __init__(self):
        self.svm = SVMUnit()
    def fit(self,input,desired):
        trainer = SVMTrainer(self.svm,zip(input,desired))
        trainer.train(log2C=0.,log2g=1.1)
    def predict(self,data):
        return self.svm.activateOnDataset(data)
