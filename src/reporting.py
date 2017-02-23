#-*- coding:utf-8; -*-

from __future__ import print_function

import loader
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas
import re

from loadclfs import kmeans,fit,predict,score
from werkzeug.utils import escape

"""
Dokument podzielony jest na trzy części:
Pierwsza z nich to funkcje do interpretera
Druga to sam interpreter
Trzecia to wiązania do interpretera używane przez widoki
Cały plik dotyczy wykonywania plików konfiguracyjnych do programu
"""

def bar_plot(df,title=None):
    """
    Generuje wykres słupkowy, konwertuje go na base64 i wkleja w HTML
    """
    plot_name = "tmp/plot.png"
    if type(df)==pandas.DataFrame:
        df.plot.bar()
    else:
        pandas.DataFrame(df).plot.bar()
    fig = plt.gcf()
    plt.draw()
    fig.savefig(plot_name)
    with open(plot_name,'rb') as f:
        data="data:image/png;base64,{}".format(f.read().encode('base64'))
    os.remove(plot_name)
    return "<img src='{}' style='width:80%;height:auto;'/>".format(data)

def vertical_table(df):
    """
    Generuje tabele odwracając dataset
    """
    header = [['index']+[x for x in df.columns]]
    body = [[str(x) for x in sublist] for sublist in df.as_matrix()]
    body = [[str(label)]+row for label,row in zip([x for x in df.index],body)]
    lists = header + body
    return "<table><tr><td>{}</td></tr></table>".format(
        "</td></tr><tr><td>".join(
            ["</td><td>".join(sub) for sub in lists]))

def mapping(df,*strings):
    """
    Tworzy nowe kolumny przy pomocy operacji arytmetycznych na starych
    """
    for s in strings:
        columnName,expression = [x.strip() for x in s.split('=',1)]
        dfColumns = [x for x in df.columns]
        for i in list(set(re.findall("([A-Za-z][A-Za-z0-9]*)",expression))):
            if i in dfColumns:
                expression = expression.replace(i,"df."+i)
        df[columnName]=eval(expression,{"df":df})
    return df

def dfsplit(ratio,df):
    """
    Losowo dzieli dataset na dwie części
    """
    mask = np.random.rand(len(df)) < ratio
    return(df[mask],df[~mask])

def setter(item,val,obj):
    """
    Wrapper do reportingu
    """
    obj[item] = val

def aggreg(list,*lists):
    """
    Tworzy nową listę przez agregację poprzedniej
    Używane w tworzeniu skali sumacyjnej
    """
    q = []
    for l in lists:
        if l[0]=='+':
            q.append(sum([list[ix] for ix in l[1:]]))
    return q

functions = {
    'log':lambda x,*formats: print(str(x).format(*formats)) or "",
    'rem':lambda *x:"",
    'print':lambda x,*formats:escape(str(x).format(*formats)).replace("\n","<br>\n").replace(" ","&nbsp;"),
    'safePrint':lambda x,*formats:x.format(*formats),
    'bar':bar_plot,
    'select':lambda df,*labels:df.select(lambda x:unicode(x) in labels,1),
    'head':lambda df,n:df.head(n),
    'query':lambda df,q:df.query(q,inplace=False),
    'corr':lambda df:df.corr(),
    'count':lambda by,df=None:(df.groupby(by=by).count().iloc[:,[0]]) if type(df)!=None else (
                                by.count()),#get length
    'verticalTable':vertical_table,
    'kmeans':kmeans,
    'drop':lambda df,*labels:df.select(lambda x:unicode(x) not in labels,1),
    'describe':lambda df:df.describe(),
    'groupBy':lambda by,df:df.groupby(by=by),
    'map':mapping,
    'fit':fit,
    'mean':lambda df:df.mean(),
    'load':lambda x:loader.loader(x,separator=','),
    'predict':predict,
    'split':dfsplit,
    'get':lambda index,object:object[index],
    'set':setter,
    'score':score,
    'aggreg':aggreg,
    '+':lambda *i:['+']+list(i)
}

class Evaluator(object):
    """
    Klasa jest interpreterem wywołań języka raportów
    Parsuje listy w sposób odpowiadający egzekucji kodu LISPa
    Posiada słownik *scope* jako otoczenie ze zmiennymi
    Obiekty tej klasy są *callable*, więc działają de facto jak
        funkcja z własnym otoczeniem, można by rzec, że taki
        obiekt jest pewnego rodzaju domknięciem.
    """
    def __init__(self,vector,scope=None):
        self.vector=vector
        self.scope = scope if scope!=None else {}
    def __call__(self,item):
        #print(self.scope.keys())
        if type(item)==list:
            if item[0][0] == "$":
                self.scope[str(item[0])] = self(item[1])
            elif item[0] == "":
                return self(item[2]) if self(item[1]) else self(item[3])
            else:
                return functions[item[0]](*map(self,item[1:]))
        elif item=="df":
            return self.vector
        elif type(item)in[str,unicode] and item[0]=="$":
            return self.scope[str(item)]
        else:
            return item

def initialize(tests):
    """
    Funkcja inicjalizuje testy, używana m.in. 
    do trenowania klasyfikatorów
    """
    scope = {}
    for test in tests:
        [query_batch(report,test['logfile'],scope) for report in test['initialize']]
    return scope

def query_report(query,vector,scope):
    """
    Funkcja konstruuje raport dla respondenta
    """
    eval = Evaluator(vector,scope)
    return eval(query)

def query_batch(query,testfilename,scope):
    """
    Funkcja konstruuje raport dla analityka
    """
    data = loader.load(testfilename)
    eval = Evaluator(data,scope)
    return eval(query)
    try: 
        return eval(query)
    except Exception as e:
        print("EXCEPTION: {}".format(escape(e.message)))
        return "<b>EXCEPTION: </b>{}".format(escape(e.message))
