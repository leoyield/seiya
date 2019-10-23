from seiya.db.base import db, RestaurantModel
from sqlalchemy import func
from seiya.analysis.toG2data import Todict

def popular_restaurant():
    data = db.session.query(RestaurantModel.taste + RestaurantModel.ambience + RestaurantModel.service, RestaurantModel.title).filter(RestaurantModel.review_count>500).all()
    data = sorted(data,key=lambda x:x[0], reverse=True)
    x = '餐馆名'
    y = '总分'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def categories_top10():
    data = db.session.query(func.count(RestaurantModel.classification), RestaurantModel.classification).group_by(RestaurantModel.classification).all()
    data = sorted(data,key=lambda x:x[0], reverse=True)
    x = '餐馆分类'
    y = '餐馆数量'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def district_top10():
    data = db.session.query(func.count(RestaurantModel.business_district), RestaurantModel.business_district).group_by(RestaurantModel.business_district).all()
    data = sorted(data,key=lambda x:x[0], reverse=True)
    x = '商圈名'
    y = '餐馆数量'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def consumption_categories_top10():
    data = db.session.query(func.avg(RestaurantModel.consumption), RestaurantModel.classification).group_by(RestaurantModel.classification).all()
    data = sorted(data,key=lambda x:x[0], reverse=True)
    x = '餐馆分类'
    y = '人均消费'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def consumption_district_top10():
    data = db.session.query(func.avg(RestaurantModel.consumption), RestaurantModel.business_district).group_by(RestaurantModel.business_district).all()
    data = sorted(data,key=lambda x:x[0], reverse=True)
    x = '商圈名'
    y = '人均消费'
    todict = Todict(y, x)
    return list(map(todict.to_dict,data[:10])), x, y

def consumption_compared():
    classification = sorted(db.session.query(func.count(RestaurantModel.classification), RestaurantModel.classification).group_by(RestaurantModel.classification).all(), reverse=True)
    classification = [x[1] for x in classification[:10]]
    result = []
    x = '餐馆分类'
    y = '人均消费'
    z = '商圈名'
    for i in classification:
        data = db.session.query(func.avg(RestaurantModel.consumption), RestaurantModel.classification, RestaurantModel.business_district).filter(RestaurantModel.classification==i).group_by(RestaurantModel.business_district).all()
        data = sorted(data,key=lambda x:x[0], reverse=True)
        todict = Todict(y, x, z)
        result += list(map(todict.to_dict,data[:10]))
    return result, x, y, z