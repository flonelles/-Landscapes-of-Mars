from flask import Flask
from flask_login import LoginManager


from api.jobs_api import jobs_blueprint
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init('db/mars_explorer.db')
login_manager = LoginManager()
login_manager.init_app(app)


app.register_blueprint(jobs_blueprint)

app.run(port=8080, host='127.0.0.1')
