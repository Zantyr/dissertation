#!env/bin/python
import flask
from loadclfs import loadclfs
app = flask.Flask(__name__)
clf = loadclfs()

jobs = []
with open('static/jobs','r') as f:
    for line in f:
        jobs.append(line.strip())

def MBTI(t):
    return ''.join(['E' if t[0] > 0 else ('I' if t[0] < 0 else "(EI)") ,
                ' S' if t[1] > 0 else (' N' if t[1] < 0 else " (SN)"),
                ' T' if t[2] > 0 else (' F' if t[2] < 0 else " (TF)"),
                ' J' if t[3] > 0 else (' P' if t[3] < 0 else " (JP)")])

def JSfy_list(l):
    return str(l)

@app.route('/quiz')
def main():
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    q,a,b=map(lambda x:list(x),zip(*questions))
    q = map(lambda x:x.encode('utf-8'),q)
    a = map(lambda x:x.encode('utf-8'),a)
    b = map(lambda x:x.encode('utf-8'),b)
    data = "var questions=" + JSfy_list(q) + "\nvar answersA=" + JSfy_list(a) + "\nvar answersB=" + JSfy_list(b)
    return flask.render_template('quiz.html',data=data,target='/results')

@app.route('/save',methods=['POST'])
def save():
    ans = flask.request.form['vector'].replace('A','0').replace('B','1')
    job = flask.request.form['job']
    job = str(jobs.index(job))
    line = ';'.join([job,ans])
    with open('static/tests','aw') as f:
        f.write(line+'\n')
    with open('static/logtests','aw') as f:
        f.write(line+'\n')
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    q = map(unicode,q)
    a = map(unicode,a)
    b = map(unicode,b)
    data = "var questions=" + JSfy_list(q) + "\nvar answersA=" + JSfy_list(a) + "\nvar answersB=" + JSfy_list(b)
    return flask.render_template('quiz.html',data=data,target='/pick')

@app.route('/learn')
def learn():
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    data = "var questions=" + JSfy_list(q) + "\nvar answersA=" + JSfy_list(a) + "\nvar answersB=" + JSfy_list(b)
    return flask.render_template('quiz.html',data=data,target='/pick')

@app.route('/pick',methods=['POST'])
def pick():
    ans = flask.request.form['vector']
    return flask.render_template('pick.html',jobs=jobs,vector=ans)

@app.route('/')
def index():
    return flask.render_template('main.html')

@app.route('/results',methods=['POST'])
def results():
    ans = flask.request.form['vector']
    ans = ans.replace('A','0').replace('B','1')
    ans = eval(ans)
    prediction = map(lambda x:{'job':x.predict([ans]),'model':x.name},clf)
    print(prediction)    
    prediction = map(lambda x:{'job':jobs[x['job']] if type(x['job'])!=tuple else MBTI(x['job']),'model':x['model']},prediction)
    line = prediction + list(ans)
    with open('static/logresults','aw') as f:
        f.write(JSfy_list(line)+'\n')
    return flask.render_template('result.html',prediction=prediction)

if __name__=="__main__":
    app.run('0.0.0.0',port=80)
