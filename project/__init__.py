from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User
from .database import Base

dbstring = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"
# eng = create_engine(dbstring)


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)

    app.config["SECRET_KEY"] = "9OLWxND4o83j4K4iuopO"
    app.config["SQLALCHEMY_DATABASE_URI"] = dbstring

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(name):

        # since the user_id is just the primary key of our user table, use it
        #  in the query for the user
        return User.query.get(name)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
