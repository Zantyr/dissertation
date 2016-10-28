#!/usr/bin/env python
import flask
import naivebayes
import svmclass
import kohonen

classifiers = {'kohonen':Kohonen,'bayes':NaiveBayes,'svm':SVM}

app = flask.Flask(__name__)
jobs = []

with open('static/jobs','r') as f:
    for line in f:
        jobs.append(line.strip())

jobflags = []
vectors = []

with open('static/tests','r') as f:
    for line in f:
        job,vector = map(lambda x: eval(x),map(lambda x:x.strip(),line.split(';')))
        vectors.append(vector)
        jobflags.append(job)

clf = classifiers['bayes']()
clf.fit(vectors,jobflags)

@app.route('/')
def main():
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    data = "var questions=" + str(q) + "\nvar answersA=" + str(a) + "\nvar answersB=" + str(b)
    return flask.render_template('quiz.html',data=data,target='/results.html')

@app.route('/save.html',methods=['POST'])
def save():
    ans = flask.request.form['vector'].replace('A','0').replace('B','1')
    job = flask.request.form['job']
    job = str(jobs.index(job))
    line = ';'.join([job,ans])
    with open('static/tests','aw') as f:
        f.write(line+'\n')
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    data = "var questions=" + str(q) + "\nvar answersA=" + str(a) + "\nvar answersB=" + str(b)
    return flask.render_template('quiz.html',data=data,target='/pick.html')

@app.route('/learn')
def learn():
    questions=[]
    with open('static/quiz','r') as f:
        for line in f:
            q,a,b=map(lambda x:x.strip(),line.split(';'))
            questions.append((q,a,b))
    q,a,b=map(lambda x:list(x),zip(*questions))
    data = "var questions=" + str(q) + "\nvar answersA=" + str(a) + "\nvar answersB=" + str(b)
    return flask.render_template('quiz.html',data=data,target='/pick.html')

@app.route('/pick.html',methods=['POST'])
def pick():
    ans = flask.request.form['vector']
    return flask.render_template('pick.html',jobs=jobs,vector=ans)

@app.route('/results.html',methods=['POST'])
def results():
    ans = flask.request.form['vector']
    ans = ans.replace('A','0').replace('B','1')
    ans = eval(ans)
    job = jobs[clf.predict(np.array([ans]))[0]]
    return flask.render_template('result.html',job=job)

app.run('0.0.0.0',port=80)
