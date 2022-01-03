from libReserve import make_lib_resv
import pandas as pd

if __name__ == '__main__':
    dataframe = pd.read_csv('info.csv', converters={u'stid': str, u'pwd': str, u'lib': str})
    for _, row in dataframe.iterrows():
        make_lib_resv(int(row['stid']), (row['pwd']), (row['lib']))


