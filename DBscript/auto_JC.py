#为JC表生成number条随机合法记录，保存为csv格式

number=1000

import pandas as pd
import random
import string

dept = ['AB','BC','CD','DE','EF','CS', 'EE', 'SE', 'AT', 'ME', 'AI', 'IE','AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ']

CNO = []
CNAME = []
PERIOD = []
CREDIT = []
TEACHER = []

for i in range(number):
        CNO.append(''.join(random.sample(dept, 1)) + '-' + ''.join(random.sample(string.digits, 2)))
        CNAME.append('课程名称' + str(i))
        credit = random.randint(2, 6)
        PERIOD.append(credit*20)
        CREDIT.append(credit)
        TEACHER.append('授课教师' + str(i))

dataframe = pd.DataFrame({'C#': CNO, 'CNAME': CNAME, 'PERIOD': PERIOD, 'CREDIT': CREDIT, 'TEACHER': TEACHER})
dataframe_drop = dataframe.drop_duplicates(subset='C#', keep='first', inplace=False)
dataframe_drop.to_csv("JC_" + str(number) + ".csv", index=False, sep=',', encoding='utf-8')