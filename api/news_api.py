import flask
from flask import jsonify

from data import db_session
from data.news import News

news_blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@news_blueprint.route('/api/news')
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('title', 'content', 'user.name'))
                 for item in news]
        }
    )