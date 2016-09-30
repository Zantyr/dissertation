class Question(object):
    def __init__(self,question,answerA,answerB):
        self.q = question
        self.a = answerA
        self.b = answerB

b=True
quest=[]
print "Reseter testow do Klasyfikatora"
while b:
    q=raw_input("Podaj pytanie: ")
    if not q:
        break
    a=raw_input("Podaj odpowiedz A: ")
    b=raw_input("Podaj odpowiedz B: ")
    quest.append(Question(q,a,b))
if quest:
    FILE="static/quiz"
    with open(FILE,'w') as f:
        for i in quest:
            f.write(';'.join([i.q,i.a,i.b])+'\n')
