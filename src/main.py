#!env/bin/python
import flask
import json
import reporting
import loader
import os
import copy

TESTS = "static/tests.json"

app = flask.Flask(__name__)
with open(TESTS,"r") as f:
    tests = json.load(f)

SCOPE = reporting.initialize(tests)

############################
#responder views

@app.route('/')
def index():
    return flask.render_template('main.html',
        tests=[x for x in enumerate(map(lambda i:i["name"],tests))])

@app.route('/quiz/<testid>')
def quiz(testid):
    with open(tests[int(testid)]["datafile"],'r') as f:
        print(tests[int(testid)]["datafile"])
        return flask.render_template('quiz.html',quizJSON=f.read(),testid=testid)

@app.route('/meta/<testid>',methods=['post'])
def meta(testid):
    return flask.render_template('pick.html',vector=flask.request.form["vector"],
        inputs=tests[int(testid)]['additional'],testid=testid)

@app.route('/results/<testid>',methods=['post'])
def result(testid):
    vector = json.loads('[{}]'.format(flask.request.form['vector']))
    for add in tests[int(testid)]['additional']:
        nv = [x for x in vector]
        nv.append({'id':add,'answer':flask.request.form[add]})
    nv = json.dumps(nv)
    loader.dump_test_data(int(testid),nv)
    vectordata = [x['answer'] for x in vector]
    reports = [reporting.query_report(report,vectordata,copy.deepcopy(SCOPE)) for report in tests[int(testid)]['reports']]
    return flask.render_template('result.html',testid=testid,vector=vector,
        reports=reports,accuracy=tests[int(testid)]['accuracy'])
    #ocena zgodnoscqi musi byc

@app.route('/rank/<testid>',methods=['post'])
def rank(testid):
    oldvector = flask.request.form['vector']
    vector = json.loads(oldvector)
    vector['accuracy'] = flask.request.form['accuracy']
    vector = json.dumps(vector)
    loader.update_test_data(int(testid),oldvector,vector)
    return flask.render_template('added.html')

##########################
#administrator views

@app.route('/report/<testid>')
def reports(testid):
    filename = tests[int(testid)]['logfile']
    reports = [reporting.query_batch(report,filename,copy.deepcopy(SCOPE)) for report in tests[int(testid)]['batch']]
    return flask.render_template('report.html',testid=testid,reports=reports)

@app.route('/console/<testid>')
def interactive(testid):
    return flask.render_template('console.html',testid=testid)

@app.route('/query/<testid>',methods=['post'])
def query(testid):
    q = flask.request.form['query']
    print q
    filename = tests[int(testid)]['logfile']
    return reporting.query_batch(json.loads(q),filename)

if __name__=="__main__":
    app.run('0.0.0.0',port=80)
