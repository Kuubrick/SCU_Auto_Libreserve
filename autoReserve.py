from libReserve import make_lib_resv
import pandas as pd
import time

if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    dataframe = pd.read_csv('info.csv', converters={u'stid': str, u'pwd': str, u'lib': str})
    for _, row in dataframe.iterrows():
        make_lib_resv(int(row['stid']), (row['pwd']), (row['lib']))
