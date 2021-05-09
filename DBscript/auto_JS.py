# 为JS表生成number条随机合法记录，保存为csv格式

number=5000

import pandas as pd
import random
import string

firstname = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
lastname = "秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘"
sex_choice = "男女"
direction = "东西南北"

SNO = []
SNAME = []
SEX = []
BDATE = []
HEIGHT = []
DORM = []

for i in range(number):
        SNO.append('0' + ''.join(random.choice(string.digits)) + '03' + ''.join(random.sample(string.digits, 4)))
        SNAME.append(str(random.choice(firstname)) + \
            ''.join(random.sample(lastname, random.randint(1, 3))))
        SEX.append(''.join(str(random.choice(sex_choice))))
        BDATE.append(''.join(str(random.randint(1990, 1995))) + '-' + \
            ''.join(str(random.randint(1, 12))) + '-' + \
            ''.join(str(random.randint(1, 28))))
        HEIGHT.append(str(round(random.uniform(1.55, 1.85), 2)))
        DORM.append(''.join(random.choice(direction)) + \
            str(random.randint(1, 30)) + '舍' + \
            str(random.randint(1, 8)) + ''.join(random.sample(string.digits, 2)))

dataframe = pd.DataFrame({'S#': SNO, 'SNAME': SNAME, 'SEX': SEX, 'BDATE': BDATE, 'HEIGHT': HEIGHT, 'DORM': DORM})
dataframe_drop = dataframe.drop_duplicates(subset='S#', keep='first', inplace=False)
dataframe_drop.to_csv("JS_" + str(number) + ".csv", index=False, sep=',', encoding='utf-8')