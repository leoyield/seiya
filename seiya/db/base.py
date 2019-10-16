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
        return url_for('jobanalysis', code=self.code)