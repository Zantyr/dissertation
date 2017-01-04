import pandas as pd

def try_to_numerify(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x

def loader(filename,separator='\t',nan='-1'):
    with open(filename,'r') as f:
        rows = [x for x in f.read().split('\n') if x]
    rows = [x.split(separator) for x in rows]
    colnames = rows[0]
    data = filter(lambda x:nan not in x[:-3],rows[1:])
    data = [[try_to_numerify(x) for x in row] for row in data]
    return pd.DataFrame(data,columns=colnames)

def load(filename):
    #load intelligently according to contents
    if filename[-4:] in ['.csv','.tsv']:
        return loader(filename)
    else:
        raise IOError("Can't load Data: {}".format(filename))

def dump_test_data(testintid,object):
    pass

def update_test_data(testintid,oldjsonstr,newjsonstr):
    pass
