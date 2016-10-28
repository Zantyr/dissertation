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
