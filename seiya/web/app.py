from flask import Flask, render_template, request, Response
import sys
sys.path.append("..")
from db.base import db, DataAnalysis, JobModel, AnalysisListModel
from flask_migrate import Migrate
from analysis import job
import json

app = Flask(__name__)
app.config.update(dict(
   SECRET_KEY = 'very secret key',
   SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:123456@localhost:3306/seiya?charset=utf8'
))
db.init_app(app)
Migrate(app, db)
db_dict = {
    'job': JobModel,
    2: 'LianJia'
}

job_analysis_dict = {
    'position-top10': ['职位数TOP10城市', job.position_top10, 'bar'],
    'salary-top10': ['薪资TOP10城市', job.salary_top10, 'bar'],
    'hot-tags': ['热门职位标签', job.hot_tags, 'bar'],
    'education-stat': ['学历要求统计', job.education_stat, 'pi'],
    'experience-stat':['工作经验统计', job.experience_stat, 'pi'],
    'salary-by-city-and-education': ['同等学历不同城市薪资对比', job.salary_by_city_and_education, 'line']
}

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = DataAnalysis.query.paginate(
        page=page,
        per_page=10,
        error_out=False
    )
    return render_template('index.html', pagination=pagination)

@app.route('/<code>')
def categroy(code):
    code = code
    if code in db_dict:
        page = request.args.get('page', default=1, type=int)

        analysis_id = DataAnalysis.query.filter_by(code=code).first().id
        
        pagination = AnalysisListModel.query.filter_by(analysis_id=analysis_id).paginate(
            page=page,
            per_page=10,
            error_out=False
        )
        title = DataAnalysis.query.filter_by(id=analysis_id).first().name
    return render_template('categroy.html', pagination=pagination, title=title)

@app.route('/job/<code>')
def jobanalysis(code):
    if job_analysis_dict[code][-1] == 'bar':
        if code == 'hot-tags':
            data, x, y, fig = job_analysis_dict[code][1]()
            title = job_analysis_dict[code][0]
            return render_template('job/jobanalysis.html', data=data, xy='{}*{}'.format(x,y), x=x, y=y, enum = enumerate(data), title=title, fig=fig, kind='bar')
        if code in job_analysis_dict:
            data, x, y = job_analysis_dict[code][1]()
            title = job_analysis_dict[code][0]
        return render_template('job/jobanalysis.html', data=data, xy='{}*{}'.format(x,y), x=x, y=y, enum = enumerate(data), title=title, kind='bar')
    elif job_analysis_dict[code][-1] == 'pi':
        data, x, y, percent = job_analysis_dict[code][1]()
        title = job_analysis_dict[code][0]
        return render_template('job/jobanalysis.html', data=data, x=x, y=y, percent=percent, enum = enumerate(data), title=title, kind='pi')
    elif job_analysis_dict[code][-1] == 'line':
        data, x, y, z = job_analysis_dict[code][1]()
        title = job_analysis_dict[code][0]
        return render_template('job/jobanalysis.html', data=data, x=x, y=y, z=z, title=title, kind='line')

@app.route("/job/hot-tags.png")
def hot_tags_png():
    return Response(job.hot_tags()[-1], content_type='image/png')


if __name__ == '__main__':

    app.run(debug=True)