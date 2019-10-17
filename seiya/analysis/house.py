from seiya.db.base import HouseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pandas as pd

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

def quantity_top10():
    data = session.query(func.count(HouseModel.community), HouseModel.community).group_by(HouseModel.community).all()
    data = sorted(data, reverse=True)
    print(data)
    x = '小区'
    y = '房源数'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def house_type_destributed():
    data = session.query(func.count(HouseModel.house_type), HouseModel.house_type).group_by(HouseModel.house_type).all()
    data = sorted(data, reverse=True)
    x = '户型'
    y = '房源数'
    percent = '占比'
    df = pd.DataFrame(data, columns=[y, x])
    per = round(df[y]/df[y].sum(), 2)
    df = pd.concat([df,per], axis=1)
    data = list(df.values)
    todict = Todict(y, x, percent)
    return list(map(todict.to_dict,data)), x, y, percent

def area_destributed():
    pass

def price_type_top10():
    data = session.query(func.avg(HouseModel.price), HouseModel.house_type, HouseModel.community).group_by(HouseModel.community, HouseModel.house_type).all()
    data = sorted(data, reverse=True)
    x = '户型'
    y = '租金'
    z = '小区'
    todict = Todict(y, x, z)
    df = pd.DataFrame(list(map(todict.to_dict,data)))
    df = df.sort_values(by=['户型','租金'], ascending=False)
    df1 = pd.DataFrame(columns=df.columns)
    count_type = set(df['户型'].values)
    for i in count_type:
        df1 = pd.concat([df1, df[df['户型']==i].iloc[:10,:]])
    data = list(df1.values)
    return list(map(todict.to_dict,data)), x, y, z