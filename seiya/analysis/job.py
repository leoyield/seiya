import sys
sys.path.append("..")
from db.base import JobModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import io

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/seiya?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

class Todict(object):
    def __init__(self, *name):
        self.name = name
    def to_dict(self, vctuple):
        vctuple = list(vctuple)
        if not isinstance(vctuple[0], int):
            vctuple[0] = round(float(vctuple[0]), 2)
        return {self.name[x]: y for x,y in enumerate(vctuple)}

def position_top10():
    data = session.query(func.count(JobModel.city), JobModel.city).group_by(JobModel.city).all()
    data = sorted(data, reverse=True)
    print(data)
    x = '城市'
    y = '职位数'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def salary_top10():
    data = session.query(func.avg((JobModel.salary_lower + JobModel.salary_upper)/2), JobModel.city).group_by(JobModel.city).all()
    data = sorted(data, reverse=True)
    x = '城市'
    y = '薪资'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def hot_tags(format='png'):
    sql = 'SELECT (tags) from jobmodel'
    df = pd.read_sql(sql=sql, con=engine)
    data = df.to_csv(index=0).split()
    data_list = []
    for tag in set(data):
        data_list.append((data.count(tag), tag))
    x = '职位标签'
    y = '出现次数'
    data_list = sorted(data_list, reverse=True)
    todict = Todict(y, x)
    df = pd.DataFrame(data_list[:10], columns=['出现次数', '职位标签'])
    # 设置中文字体，如果系统里没有 SimHei 字体，可以替换为其它任何中文字体
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 避免 - 号显示为方块
    mpl.rcParams['axes.unicode_minus'] = False
    # 设置画布宽高，单位为英寸
    mpl.rcParams['figure.figsize'] = 11, 5
    plt.bar(range(len(df)),df['出现次数'], color='c', tick_label=df['职位标签'])
    fig = io.BytesIO()
    plt.savefig(fig, format=format)
    return list(map(todict.to_dict, data_list[:10])), x, y, fig.getvalue()

def education_stat():
    data = session.query(func.count(JobModel.education), JobModel.education).group_by(JobModel.education).all()
    data = sorted(data, reverse=True)
    x = '学历'
    y = '统计次数'
    percent = '占比'
    df = pd.DataFrame(data, columns=[y, x])
    per = round(df[y]/df[y].sum(), 2)
    df = pd.concat([df,per], axis=1)
    data = list(df.values)
    todict = Todict(y, x, percent)
    return list(map(todict.to_dict,data)), x, y, percent

def experience_stat():
    data = session.query(JobModel.experience_lower, JobModel.experience_upper).all()
    x = '工作年限'
    y = '统计次数'
    percent = '占比'
    total = len(data)
    result = []
    for year in set(data):
        if year == (0, 0):
            result.append({x:'不限', y: data.count(year), percent: round(data.count(year)/total, 2)})
        else:
            result.append({x:'{}-{}年'.format(year[0], year[1]), y: data.count(year), percent: round(data.count(year)/total, 2)})
    result = sorted(result, key=lambda y: y['统计次数'], reverse=True)
    return result, x, y, percent

def salary_by_city_and_education():
    data = session.query(func.avg((JobModel.salary_lower + JobModel.salary_upper)/2), JobModel.education, JobModel.city).group_by(JobModel.city, JobModel.education).all()
    # data = sorted(data, reverse=True)
    x = '学历'
    y = '薪资'
    z = '城市'

    todict = Todict(y, x, z)
    return list(map(todict.to_dict,data)), x, y, z