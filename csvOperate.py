import pandas as pd


def insert(stid, pwd, lib):
    data = [[stid, pwd, lib]]
    dataframe = pd.DataFrame(data, columns=['stid', 'pwd', 'lib'])
    dataframe.to_csv("info.csv", index=False, sep=',', mode='a', header=0)


def in_the_csv(stid):
    dataframe = pd.read_csv('info.csv', usecols=[0])
    for _, row in dataframe.iterrows():
        if str(stid) == str(row['stid']):
            return True
    return False


def is_same_lib(lib):
    dataframe = pd.read_csv('info.csv', usecols=[2])
    for _, row in dataframe.iterrows():
        if str(lib) == str(row['lib']):
            return True
    return False


if __name__ == '__main__':
    print(in_the_csv(stid=5456444654))
