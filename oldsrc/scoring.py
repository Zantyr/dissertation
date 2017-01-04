from collections import Counter

class HollandScoring(object):
    def __init__(self):
        self.name = "Punktacja psychologiczna - Holland"
    def fit(self,*args):
        return self
    def predict(self,data):
        vector = ((0,1),(0,2),(0,3),(0,5),(1,3),(1,2),(1,4),(1,5),(2,3),
                  (2,4),(0,4),(2,5),(3,4),(3,5),(4,5),(0,3),(1,4),(2,5),(5,4),(3,2),
                  (1,0),(1,2),(3,4),(5,0),(0,2),(1,3),(2,4),(3,5),(4,0),(5,1))
        choices = [x[y] for x,y in zip(vector,data[0][:30])]
        print(Counter(choices))
        return Counter(choices).most_common(1)[0][0]

class MBScoring(object):
    def __init__(self):
        self.name = "Punktacja psychologiczna - Myers-Briggs"
    def fit(self,*args):
        return self
    def predict(self,data):
        data = data[0][30:]
        EI,SN,TF,JP = 0,0,0,0
        EI -= 1 if data[7] else -1
        EI -= -1 if data[6] else 1
        SN -= 1 if data[5] else -1
        SN -= -1 if data[3] else 1
        TF -= 1 if data[4] else -1
        TF -= -1 if data[2] else 1
        JP -= 1 if data[1] else -1
        JP -= -1 if data[0] else 1
        EI -= sum([1 if x else -1 for x in data[8:11]])
        SN -= sum([1 if x else -1 for x in data[11:14]])
        TF -= sum([1 if x else -1 for x in data[14:17]])
        JP -= sum([1 if x else -1 for x in data[17:20]])
        print((EI,SN,TF,JP))
        return (EI,SN,TF,JP)
