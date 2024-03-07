import flask
from flask import jsonify

from data import db_session
from data.news import News

jobs_blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@jobs_blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('title', 'content', 'user.name'))
                 for item in news]
        }
    )