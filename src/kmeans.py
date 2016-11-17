from sklearn.cluster import KMeans as sKMeans
import numpy as np
from collections import Counter
from selectors import PersonalitySelector,JobSelector

class KMeans(object):
    def __init__(self):
        self.classes = 6
        self.name = "Metoda Ksrednich - klasteryzacja"
        self.kmeans = sKMeans(n_clusters=self.classes,init='random')
    def fit(self,input,desired,_):
        self.kmeans = self.kmeans.fit(np.array(input))
        self.match = zip(self.kmeans.labels_,desired)
        self.match.sort(key=lambda x:x[0])
        self.mapping = [[y[1] for y in self.match if y[0]==x] for x in range(self.classes)]
        self.mapping = [Counter(x).most_common(1)[0][0] for x in self.mapping]
        return self
    def predict(self,data):
        return [self.mapping[x] for x in self.kmeans.predict(np.array(data,dtype='double'))][0]
        
class JobKMeans(JobSelector):
    def __init__(self):
        super(JobKMeans,self).__init__()
        self.model = KMeans()

class PersonalityKMeans(PersonalitySelector):
    def __init__(self):
        super(PersonalityKMeans,self).__init__()
        self.model = KMeans()


if __name__=="__main__":
    s = KMeans().fit([[0,8],[-2,-3],[5,4],[4,4],[-2,-3],[1,1],[8,8],[5,5],[4,3],[1,0],[0,1],[1,2]],[0,1,2,3,4,5,0,1,2,3,4,5])
    print s.predict([[3,3],[1,1],[-2,-2]])
