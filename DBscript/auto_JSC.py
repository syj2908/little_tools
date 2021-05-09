#为JSC表生成number条随机合法记录，保存为csv格式

number = 20000
JSpath = r'D:\Algorithm\JS_5000.csv'
JCpath = r'D:\Algorithm\JC_1000.csv'

import pandas as pd
import random
import string

JS = pd.read_csv(JSpath, encoding='utf-8', dtype=object)
JC = pd.read_csv(JCpath, encoding='utf-8', dtype=object)

SNO = []
CNO = []
GRADE = []

for i in range(number):
    SNO.append(str(JS['S#'][random.randint(0, len(JS)-1)]))
    CNO.append(str(JC['C#'][random.randint(0, len(JC)-1)]))
    GRADE.append(str(random.randint(40, 100)))

dataframe = pd.DataFrame({'S#': SNO, 'C#': CNO, 'GRADE': GRADE})
dataframe_drop = dataframe.drop_duplicates(subset=['S#', 'C#'], keep='first', inplace=False)
dataframe_drop.to_csv("JSC_" + str(number) + ".csv", index=False, sep=',', encoding='utf-8')