from flask import Flask
from flask_cors import CORS

import os

from .src.blueprints.geolocation.routes import geolocation_bp
from .src.blueprints.geolocation.config import getApp as getAppGeolocation


def createApp():
    app = Flask(__name__)
    app = getAppGeolocation(app)
    CORS(app)

    # mysql : https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip/25865271
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidvisitorsadmin:davidvisitorspassword@localhost/davidvisitors'
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_DAVIDVISITORS')
    # app.secret_key = os.environ.get('SECRET_KEY_DAVIDVISITORS')
    # app.config['PERMANENT_SESSION_LIFETIME'] = 3600
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # https://flask-admin.readthedocs.io/en/latest/introduction

    # set optional bootswatch theme
    # See https://bootswatch.com/3/ for available swatches
    # app.config['FLASK_ADMIN_SWATCH'] = 'superhero'

    # admin = Admin(app, name='Admin interface :)', template_mode='bootstrap3')

    app.register_blueprint(geolocation_bp)

    with app.app_context() :
        # from .models import db, Visit, User, Message

        # admin.add_view(ModelView(Visit, db.session))
        # admin.add_view(ModelView(User, db.session))
        # admin.add_view(ModelView(Message, db.session))
        
        # db.init_app(app)
        # db.create_all()

        return app

# def get_socketio(app) :
#     with app.app_context() :
#         from .socketio import socketio

#         return socketio