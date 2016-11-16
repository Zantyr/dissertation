class Selector(object):
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,value):
        self._model = value
        self._model.name += self.tag
    def fit(self,data,desired):
        data = [self.generate_selector()(sset) for sset in data]
        return self.model.fit(data,desired)
    def predict(self,data):
        data = [self.generate_selector()(sset) for sset in data]
        return self.model.predict(data)
    def generate_selector(self):
        return lambda data: [z[1] for z in filter(lambda (x,y): True if x in self.selection else False,enumerate(data))]

class JobSelector(Selector):
    selection = range(10)
    tag = " - tylko pytania Hollanda"

class PersonalitySelector(Selector):
    selection = []
    tag = " - tylko pytania MBTI"
