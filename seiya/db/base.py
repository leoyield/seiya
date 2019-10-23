from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import url_for

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

class DataAnalysis(Base):
    __tablename__ = 'dataanalysis'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    code = db.Column(db.String(32), unique=True, index=True)
    description = db.Column(db.String(256))
    tlagou = db.relationship('JobModel')
    tlianjia = db.relationship('HouseModel')
    tdianping = db.relationship('RestaurantModel')
    analysislist = db.relationship('AnalysisListModel')

    @property
    def url(self):
        return url_for('categroy', code=self.code)

class JobModel(Base):
    __tablename__ = 'jobmodel'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    city = db.Column(db.String(64), nullable=True)
    salary_lower = db.Column(db.Integer, nullable=True)
    salary_upper = db.Column(db.Integer, nullable=True)
    experience_lower = db.Column(db.Integer, nullable=True)
    experience_upper = db.Column(db.Integer, nullable=True)
    education = db.Column(db.String(16), nullable=True)
    tags = db.Column(db.String(256), nullable=True)
    company = db.Column(db.String(32), nullable=True)
    analysis_id = db.Column(db.Integer, db.ForeignKey('dataanalysis.id', ondelete='CASCADE'), default=1)
    analysis = db.relationship('DataAnalysis', backref=db.backref('jobmodel', cascade='all, delete-orphan'))

class HouseModel(Base):
    __tablename__ = 'housemodel'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    region = db.Column(db.String(64), nullable=True)
    street = db.Column(db.String(64), nullable=True)
    community = db.Column(db.String(64), nullable=False)
    area = db.Column(db.Integer, nullable=True)
    direction = db.Column(db.String(64), nullable=True)
    house_type = db.Column(db.String(64), nullable=True)
    floor = db.Column(db.String(64), nullable=True)
    building_height = db.Column(db.Integer, nullable=True)
    tags = db.Column(db.String(256), nullable=True)
    price = db.Column(db.Integer, nullable=False)

    analysis_id = db.Column(db.Integer, db.ForeignKey('dataanalysis.id', ondelete='CASCADE'), default=2)
    analysis = db.relationship('DataAnalysis', backref=db.backref('housemodel', cascade='all, delete-orphan'))

class RestaurantModel(Base):
    __tablename__ = 'restaurantmodel'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    score = db.Column(db.Integer, nullable=True)
    review_count = db.Column(db.Integer, nullable=True)
    consumption = db.Column(db.Integer, nullable=True)
    classification = db.Column(db.String(64), nullable=True)
    business_district = db.Column(db.String(64), nullable=True)
    taste = db.Column(db.Float, nullable=True)
    ambience = db.Column(db.Float, nullable=True)
    service = db.Column(db.Float, nullable=True)

    analysis_id = db.Column(db.Integer, db.ForeignKey('dataanalysis.id', ondelete='CASCADE'), default=3)
    analysis = db.relationship('DataAnalysis', backref=db.backref('restaurantmodel', cascade='all, delete-orphan'))

class AnalysisListModel(Base):
    __tablename__ = 'analysislistmodel'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    code = db.Column(db.String(32), unique=True, index=True)
    description = db.Column(db.String(256))
    analysis_id = db.Column(db.Integer, db.ForeignKey('dataanalysis.id', ondelete='CASCADE'))
    analysis = db.relationship('DataAnalysis', backref=db.backref('analysislistmodel', cascade='all, delete-orphan'))

    @property
    def url(self):
        if self.analysis_id == 1:
            return url_for('jobanalysis', code=self.code)
        elif self.analysis_id == 2:
            return url_for('houseanalysis', code=self.code)
        elif self.analysis_id == 3:
            return url_for('restaurantanalysis', code=self.code)


def create_data():
    print('in craete')
    if not DataAnalysis.query.first():
        print('im in DataAnalysis')
        d1 = DataAnalysis(name='勾网职位数据分析', description='热门工作城市,薪资最高城市,热门职位标签', code='job')
        d2 = DataAnalysis(name='链家网租房数据分析', description='门租房小区,租金最贵的小区,房龄分布', code='enthouse')
        d3 = DataAnalysis(name='点评网餐馆数据分析', description='热门菜系,热门商圈,最受欢迎的菜系', code='restaurant')
        db.session.add(d1)
        db.session.add(d2)
        db.session.add(d3)
        db.session.commit()
        print('success create DataAnalysis')
    elif not AnalysisListModel.query.first():
        print('im in AnalysisListModel')
        a1 = AnalysisListModel(name='职位数 TOP10 城市', code='position-top10', description='按发布职位排名前十的城市', analysis_id='1')
        a2 = AnalysisListModel(name='薪资 TOP10 城市', code='salary-top10', description='按发布薪资排名前十的城市', analysis_id='1')
        a3 = AnalysisListModel(name='热门职位标签', code='hot-tags', description='按发布出现次数统计前十的职位标签', analysis_id='1')
        a4 = AnalysisListModel(name='工作经验统计', code='experience-stat', description='所有发布职位里每种工作经验范围的占比', analysis_id='1')
        a5 = AnalysisListModel(name='学历要求统计', code='education-stat', description='所有发布职位里每种工作要求学历的占比', analysis_id='1')
        a6 = AnalysisListModel(name='同等学历不同城市薪资对比', code='salary-by-city-and-education', description='同等学历要求的职位在不同城市里的薪资对比', analysis_id='1')
        a7 = AnalysisListModel(name='房源数量TOP10小区', code='quantity-top10', description='分析得到房源数量排名前十的小区', analysis_id='2')
        a8 = AnalysisListModel(name='户型分布统计', code='house-type-destributed', description='统计所有房源里每种户型所占的百分比', analysis_id='2')
        a9 = AnalysisListModel(name='面积分布统计', code='area-destributed', description='分析所有房源的面积分布情况', analysis_id='2')
        a10 = AnalysisListModel(name='每种户型租金最贵TOP10小区', code='price-type-top10', description='分析得到每种户型租金排名前十的小区', analysis_id='2')
        a11 = AnalysisListModel(name='最受欢迎的餐馆', code='popular-restaurant', description='综合评论数、口味、环境、服务几个指标，得到好评度排名前十的餐馆', analysis_id='3')
        a12 = AnalysisListModel(name='热门餐馆数量TOP10分类', code='categories-top10', description='统计餐馆数排名前十的分类', analysis_id='3')
        a13 = AnalysisListModel(name='热门餐馆数量TOP10商圈', code='district-top10', description='统计餐馆数排名前十的商圈', analysis_id='3')
        a14 = AnalysisListModel(name='人均消费最贵的分类', code='consumption-categories-top10', description='统计人均消费排名前十的分类', analysis_id='3')
        a15 = AnalysisListModel(name='人均消费最贵的商圈', code='consumption-district-top10', description='统计人均消费排名前十的商圈', analysis_id='3')
        a16 = AnalysisListModel(name='热门分类在热门商圈的人均消费对比', code='consumption-compared', description='统计每个热门分类（餐馆数排名前十）在每个热门商圈（餐馆数排名前十）的人均消费', analysis_id='3')
        for i in range(1,17):
            db.session.add(eval('a{}'.format(i)))
        db.session.commit()
        print('success create AnalysisListModel')