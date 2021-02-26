import datetime
from sqlalchemy import *
from flask_sqlalchemy import sqlalchemy
from flask import Flask
import flask_login
from logging.config import dictConfig
from .auth import *
from .models import *
from .main import *
from flask_login import LoginManager


dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"


app = Flask(__name__)

app.config["SECRET_KEY"] = "9OLWxND4o83j4K4iuopO"
app.config["SQLALCHEMY_DATABASE_URI"] = dbs
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"


login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(name):
    return User.query.get(name)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(bp)

    return app

    if __name__ == "__main__":
        app.run()
