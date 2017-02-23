#!env/bin/python
#-*- coding:utf-8; -*-

import flask
import json
import reporting
import loader
import os
import copy

#Ustawienie domyślnego pliku z konfiguracją testów
TESTS = "static/tests.json"

#Tworzenie aplikacji webowej
app = flask.Flask(__name__)
with open(TESTS,"r") as f:
    tests = json.load(f)

#Wczytanie przestrzeni zmiennych do języka skryptowego
#Przekazywane do metod interpretujących pliki konfiguracyjne
SCOPE = reporting.initialize(tests)

############################
#Widoki respondenta

#Widok główny
@app.route('/')
def index():
    return flask.render_template('main.html',
        tests=[x for x in enumerate(map(lambda i:i["name"],tests))])

#Widok quizu
@app.route('/quiz/<testid>')
def quiz(testid):
    with open(tests[int(testid)]["datafile"],'r') as f:
        print(tests[int(testid)]["datafile"])
        return flask.render_template('quiz.html',quizJSON=f.read(),testid=testid)

#Widok podawania dodatkowych informacji
@app.route('/meta/<testid>',methods=['post'])
def meta(testid):
    return flask.render_template('pick.html',vector=flask.request.form["vector"],
        inputs=tests[int(testid)]['additional'],testid=testid)

#Generowanie rezultatów
@app.route('/results/<testid>',methods=['post'])
def result(testid):
    vector = json.loads('[{}]'.format(flask.request.form['vector']))
    nv = [x for x in vector]
    for add in tests[int(testid)]['additional']:
        nv.append({'id':add,'answer':flask.request.form[add]})
        print add
    nv = json.dumps(nv)
    loader.dump_test_data(tests[int(testid)]["logfile"],nv)
    vectordata = [x['answer'] for x in vector]
    reports = [reporting.query_report(report,vectordata,copy.deepcopy(SCOPE)) for report in tests[int(testid)]['reports']]
    return flask.render_template('result.html',testid=testid,vector=vector,
        reports=reports)

##########################
#Widoki administratora

#Generowanie raportów na podstawie pliku konfiguracyjnego
@app.route('/report/<testid>')
def reports(testid):
    filename = tests[int(testid)]['logfile']
    reports = [reporting.query_batch(report,filename,copy.deepcopy(SCOPE)) for report in tests[int(testid)]['batch']]
    return flask.render_template('report.html',testid=testid,reports=reports)

#Konsola do dynamicznego testowania konfiguracji
@app.route('/console/<testid>')
def interactive(testid):
    return flask.render_template('console.html',testid=testid)

#Obsługa POST do powyższego widoku
@app.route('/query/<testid>',methods=['post'])
def query(testid):
    q = flask.request.form['query']
    print q
    filename = tests[int(testid)]['logfile']
    return reporting.query_batch(json.loads(q),filename,copy.deepcopy(SCOPE))

#Uruchomienie aplikacji
if __name__=="__main__":
    app.run('0.0.0.0',port=80)
