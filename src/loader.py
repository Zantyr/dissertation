#-*- coding:utf-8; -*-
import pandas as pd
import json

def try_to_numerify(x):
    """
    Jeśli to możliwe, przekonwertuj na liczbę
    """
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

def loader(filename,separator='\t',nan='-1'):
    """
    Funkcja wczytuje pliki csv
    Można użyć pandas.from_csv, jednak zostało już wprowadzone w kod
        i pozostaje dla kompatybilności
    """
    with open(filename,'r') as f:
        rows = [x for x in f.read().split('\n') if x]
    rows = [x.split(separator) for x in rows]
    colnames = rows[0]
    data = filter(lambda x:nan not in x,rows[1:]) #ignore all malformed inputs
    data = [[try_to_numerify(x) for x in row] for row in data]
    return pd.DataFrame(data,columns=colnames)

def load(filename):
    """
    Funkcja wczytywania - rozbudowanie jej pozwala ładować pliki
        w innych formatach niż csv/tsv
    """
    if filename[-4:] in ['.csv','.tsv']:
        return loader(filename)
    else:
        raise IOError("Can't load Data: {}".format(filename))

def dump_test_data(logfilename,obj):
    """
    Funkcja zapisuje rekord do pliku z logami
    """
    data = [x['answer'] for x in json.loads(obj)]
    with open(logfilename,'a') as f:
        f.write("\n{}".format("\t".join([str(x) for x in data])))
