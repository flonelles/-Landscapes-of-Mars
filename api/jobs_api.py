import flask
from flask import jsonify

from data import db_session
from data.jobs import Jobs

jobs_blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@jobs_blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('id', 'job'))
                 for item in jobs]
        }
    )