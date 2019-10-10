from flask import Flask, render_template, request
import sys
sys.path.append("..")
from db.base import db, DataAnalysis, JobModel
from flask_migrate import Migrate

app = Flask(__name__)
app.config.update(dict(
   SECRET_KEY = 'very secret key',
   SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root:123456@localhost:3306/seiya?charset=utf8'
))
db.init_app(app)
Migrate(app, db)
db_dict = {
    1: JobModel,
    2: 'LianJia'
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

@app.route('/categroy/<int:id>')
def categroy(id):
    if id in db_dict:
        page = request.args.get('page', default=1, type=int)
        pagination = db_dict[id].query.paginate(
            page=page,
            per_page=10,
            error_out=False
        )
    return render_template('categroy.html', pagination=pagination)

if __name__ == '__main__':

    app.run(debug=True)