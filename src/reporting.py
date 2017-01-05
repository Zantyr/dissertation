from __future__ import print_function
import loader
import pandas
import matplotlib.pyplot as plt
import os
from werkzeug.utils import escape
from loadclfs import kmeans,fit
import re

def bar_plot(df,title=None):
    plot_name = "tmp/plot.png"
    df.plot.bar()
    fig = plt.gcf()
    plt.draw()
    fig.savefig(plot_name)
    with open(plot_name,'rb') as f:
        data="data:image/png;base64,{}".format(f.read().encode('base64'))
    os.remove(plot_name)
    return "<img src='{}' style='width:80%;height:auto;'/>".format(data)

def radar_plot(df):
    plot_name = "tmp/plot.png"
    m = df.as_matrix()
    labels = [6.28/len(m)*x for x in range(len(m))]
    plt.bar(labels,m,c=m,cmap=plt.cm.jet)
    fig = plt.gcf()
    plt.draw()
    fig.savefig(plot_name)
    with open(plot_name,'rb') as f:
        data="data:image/png;base64,{}".format(f.read().encode('base64'))
    os.remove(plot_name)
    return "<img src='{}' style='width:80%;height:auto;'/>".format(data)

def vertical_table(df):
    header = [['index']+[x for x in df.columns]]
    body = [[str(x) for x in sublist] for sublist in df.as_matrix()]
    body = [[str(label)]+row for label,row in zip([x for x in df.index],body)]
    lists = header + body
    return "<table><tr><td>{}</td></tr></table>".format(
        "</td></tr><tr><td>".join(
            ["</td><td>".join(sub) for sub in lists]))

def mapping(df,*strings):
    for s in strings:
        columnName,expression = [x.strip() for x in s.split('=',1)]
        dfColumns = [x for x in df.columns]
        for i in list(set(re.findall("([A-Za-z][A-Za-z0-9]*)",expression))):
            if i in dfColumns:
                expression = expression.replace(i,"df."+i)
        df[columnName]=eval(expression,{"df":df})
    return df

def pythoneval(expr,*scope):
    #link with evaluator
    scope = dict(["$"+(str(x),y) for x,y in enumerate(scope)])
    return eval(expr)

functions = {
    'log':lambda x,*formats: print(x.format(*formats)) or "",
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
    'star':radar_plot,
    'mean':lambda df:df.mean(),
}

class Evaluator(object):
    def __init__(self,vector,scope=None):
        self.vector=vector
        self.scope = scope if scope!=None else {}
    def __call__(self,item):
        if type(item)==list:
            if item[0][0] == "$":
                self.scope[str(item[0])] = self(item[1])
                return ""
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
    scope = {}
    for test in tests:
        [query_batch(report,test['logfile'],scope) for report in test['initialize']]
    return scope

def query_report(query,vector):
    eval = Evaluator(vector)
    return eval(query)

def query_batch(query,testfilename,scope):
    data = loader.load(testfilename)
    eval = Evaluator(data,scope)
    try:
        return eval(query)
    except Exception as e:
        return "<b>EXCEPTION: </b>{}".format(escape(e.message))