from fann2 import libfann

class Kohonen(object):
    def __init__(self,rate,layers):
        self.net = libfann.neural_net()
        self.net.create_sparse_array(rate,layers)
        self.net.set_learning_rate(rate)
    def fit(self,input,desired):
        self.net.train(input,desired)
    def predict(self.data):
        return self.net.run(x)
    def save(self,filename):
        self.net.save(filename)
    @classmethod
    def load(cls,filename):
        obj=cls()
        obj.net.create_from_file(filename)
